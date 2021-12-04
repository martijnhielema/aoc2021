import re
import numpy as np
from itertools import chain
import math

with open('input.txt') as f:
    input = f.read()
    parts = input.split('\n\n')
    numbers = list(map(int, parts[0].split(',')))
    raw_boards = [x.split('\n') for x in parts[1:]]
    parsed_boards = []
    for board in raw_boards:
        parsed_boards.append([list(map(int, re.split('[ ]+', x.strip()))) for x in board])


def draw_number(number, boards):
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            boards[i][j] = ['X' if x == number else x for x in row]

    return boards


def check_board_bingo(board):
    for row in board:
        if set(row) == {'X'}:
            return True
    return False


def flatten_and_multiply(bingo_board):
    flat = [0 if x == 'X' else x for x in chain.from_iterable(bingo_board)]

    return int(math.fsum(flat))


print('First part')
bingo = False
for number in numbers:
    if bingo:
        break
    draw_number(number, parsed_boards)
    for i, board in enumerate(parsed_boards):
        if check_board_bingo(board) or check_board_bingo(np.transpose(board.copy())):
            print('BINGO!')
            print(board)
            remainder = flatten_and_multiply(board)
            print(f'Number is {number} and sum is {remainder}. Multiplied: {remainder * number}')
            bingo = True
            continue

print('\nPart 2')
for number in numbers:
    draw_number(number, parsed_boards)
    to_delete = []
    for i, board in enumerate(parsed_boards):
        if check_board_bingo(board) or check_board_bingo(np.transpose(board.copy())):
            if len(parsed_boards) == 1:
                print(parsed_boards)
                remainder = flatten_and_multiply(parsed_boards[0])
                print(f'Number is {number} and sum is {remainder}. Multiplied: {remainder * number}')
                exit()
            to_delete.append(i)

    for j in sorted(to_delete, reverse=True):
        parsed_boards.pop(j)
