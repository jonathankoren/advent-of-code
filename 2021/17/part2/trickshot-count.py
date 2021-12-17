#!/usr/bin/env python3

def read_target_area():
     (target, area, xstr, ystr)= input().split(' ')
     xstr = xstr[2:-1]
     ystr = ystr[2:]

     (xmin, xmax) = list(map(lambda x: int(x), xstr.split('..')))
     (ymin, ymax) = list(map(lambda x: int(x), ystr.split('..')))
     return (xmin, xmax, ymin, ymax)

def update(xpos, ypos, xspeed, yspeed):
    xpos += xspeed
    ypos += yspeed
    yspeed -= 1
    if xspeed != 0:
        xsign = 1
        if xspeed < 0:
            xsign = -1
        xspeed = xsign * (abs(xspeed) - 1)

    return (xpos, ypos, xspeed, yspeed)

def in_target(target_xmin, target_xmax, target_ymin, target_ymax, xpos, ypos):
    return (target_xmin <= xpos) and (xpos <= target_xmax) and \
            (target_ymin <= ypos) and (ypos <= target_ymax)

def terminate(target_xmin, target_xmax, target_ymin, target_ymax, xpos, ypos):
    return (xpos > target_xmax) or (ypos < target_ymin)


def simulate(xspeed_init, yspeed_init, target_xmin, target_xmax, target_ymin, target_ymax):
    xpos = 0
    ypos = 0
    xspeed = 0
    yspeed = 0

    max_y = 0
    xspeed = xspeed_init
    yspeed = yspeed_init
    while True:
        if ypos > max_y:
            max_y = ypos
        if in_target(target_xmin, target_xmax, target_ymin, target_ymax, xpos, ypos):
            return max_y
        if terminate(target_xmin, target_xmax, target_ymin, target_ymax, xpos, ypos):
            return None
        (xpos, ypos, xspeed, yspeed) = update(xpos, ypos, xspeed, yspeed)

##############################################################################

(target_xmin, target_xmax, target_ymin, target_ymax) = read_target_area()

best_xspeed = 0
best_yspeed = 0
max_y = 0

count = 0
for xspeed_init in range(target_xmax * 2):
    for yspeed_init in range(min(target_ymin, target_ymax), max(abs(target_ymin), abs(target_ymax))):
        hit = simulate(xspeed_init, yspeed_init, target_xmin, target_xmax, target_ymin, target_ymax)
        if hit is not None:
            count += 1
print(count)
