#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#


def solve(crossword, row, col, word, index):
    if row == len(crossword) or col == len(crossword[0]) or crossword[row][col] == '+':
        if index == len(word):
            return
        return
    crossword[row][col] = word[index]
    solve(crossword, row+1, col, word, index+1)
    solve(crossword, row, col+1, word, index+1)
    crossword[row][col] = '-'


def crosswordPuzzle(crossword, words):
    for word in words:
        for i in range(len(crossword)):
            for j in range(len(crossword[0])):
                solve(crossword, i, j, word, 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
