#!/usr/bin/env python3

from bitstring import BitStream

def hexdecode(c):
    try:
        return int(c)
    except ValueError:
        return (ord(c) - 65) + 10

def bitmask(num_bits):
    m = 0
    for i in range(num_bits):
        m += (2 ** i)
    return m


TYPE_LITERAL = 4

class Packet:
    def __init__(self):
        self.version = None
        self.type = None
        self.payload = []

    def _repr(self, level=0):
        s = ""
        for i in range(level):
            s += "\t"
        s += f"v:{self.version} t:{self.type} p:"
        if self.type == 4:
            s += str(self.payload[0])
        else:
            for p in self.payload:
                s += "\n" + p._repr(level + 1)
        return s

    def __repr__(self):
        return self._repr()

def readpacket(bs):
    packet = Packet()
    bits_read = 0
    packet.version = bs.read(3).uint
    packet.type = bs.read(3).uint

    bits_read += 6
    if packet.type == TYPE_LITERAL:
        # literal
        keep_reading = True
        n = 0
        while keep_reading:
            keep_reading = bs.read(1).uint > 0
            n = (n << 4) + bs.read(4).uint
            bits_read += 5
        packet.payload.append(n)
    else:
        # operator
        length_type = bs.read(1).uint
        bits_read += 1
        if length_type == 1:
            # read next 11 bits. Then read that many packets
            num_packets_in_payload = bs.read(11).uint
            bits_read += 11
            for i in range(num_packets_in_payload):
                (subpacket, read) = readpacket(bs)
                bits_read += read
                packet.payload.append(subpacket)
        else:
            # Read next 15 bits. Then read that many bits as the payload
            num_bits_in_payload = bs.read(15).uint
            bits_read += 15
            subpacket_bits = 0
            while subpacket_bits < num_bits_in_payload:
                (subpacket, read) = readpacket(bs)
                subpacket_bits += read
                packet.payload.append(subpacket)
            bits_read += subpacket_bits
    return (packet, bits_read)

def sum_versions(packet):
    v = packet.version
    if packet.type != TYPE_LITERAL:
        for p in packet.payload:
            v += sum_versions(p)
    return v


##############################################################################

(packet, bits_read) = readpacket(BitStream('0x' + input()))
print(sum_versions(packet))
