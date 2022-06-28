import sys
from collections import defaultdict

sys.stdin = open('input.txt')

T = int(input())


def GoUp():
    global i, r, val
    for _ in range(2 * i + 1):
        r -= 1
        val += 1
        AddArray(val)

def GoLeft():
    global i, c, val
    for _ in range(2 * i + 2):
        c -= 1
        val += 1
        AddArray(val)

def GoDown():
    global i, r, val
    for _ in range(2 * i + 2):
        r += 1
        val += 1
        AddArray(val)

def GoRight():
    global i, c, val
    for _ in range(2 * i + 2):
        c += 1
        val += 1
        AddArray(val)

def AddArray(val):
    global r1, c1, r2, c2, r, c, maximal
    if r1 <= r <= r2 and c1 <= c <= c2:
        array[r][c] = val
        maximal = max(maximal, val)


for _ in range(T):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    limit = max(abs(r1), abs(c1), abs(r2), abs(c2))

    array = defaultdict(defaultdict)

    r = 0
    c = 0
    val = 1
    maximal = 1

    AddArray(val)
    for i in range(limit):
        c += 1
        val += 1
        AddArray(val)

        GoUp()
        GoLeft()
        GoDown()
        GoRight()

    lmax = len(str(maximal))
    for row in range(r1, r2 + 1):
        answer = ''
        for col in range(c1, c2 + 1):
            blank = len(str(array[row][col]))
            answer += ' ' * (lmax - blank)
            answer += str(array[row][col])
            answer += ' '
        answer.rstrip()
        print(answer)