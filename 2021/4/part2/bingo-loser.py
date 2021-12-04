#!/usr/bin/env python3

import re
import sys

class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.marked = [None] * 5
        for i in range(5):
            self.marked[i] = [False] * 5

    def mark(self, number):
        '''Marks the numebr on the board, and returns True if
        the card wins, return False if not a winner.'''
        for i in range(5):
            for j in range(5):
                if self.numbers[i][j] == number:
                    self.marked[i][j] = True
                    return  self.is_winner()
        return False

    def is_winner(self):
        '''Returns True if all the cells in a row, or all the cells
        in a column are marked. Otheriwse returns False.'''
        # check rows
        for i in range(5):
            winner = True
            for j in range(5):
                if not self.marked[i][j]:
                    winner = False
                    break
            if winner:
                return True

        # check cols
        for j in range(5):
            winner = True
            for i in range(5):
                if not self.marked[i][j]:
                    winner = False
                    break
            if winner:
                return True

        # not a winner
        return False

    def sum_unmarked(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                if not self.marked[i][j]:
                    sum += self.numbers[i][j]

        return sum

def read_board():
    numbers = []
    input()  # skip the blank
    for i in range(5):
        numbers.append(list(map(lambda x: int(x), filter(lambda x: x != '', re.split(' +', input())))))
    return Board(numbers)



# read called numbers
called_numbers = map(lambda x: int(x), input().split(','))

# read boards
boards = []
try:
    while True:
        boards.append(read_board())
except EOFError:
    pass

winners = set()
for last_number in called_numbers:
    for i in range(len(boards)):
        if i not in winners:
            if boards[i].mark(last_number):
                winners.add(i)
                if len(winners) == len(boards):
                    print(last_number * boards[i].sum_unmarked())
                    sys.exit(0)

print("NO WINNER! NO CHICKEN DINNER!")
