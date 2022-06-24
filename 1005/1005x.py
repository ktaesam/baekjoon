# gold 3

import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N, R = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))

    need = dict()
    for i in range(1, N + 1):
        need[i] = []

    for r in range(R):
        from_num, to_num = map(int, sys.stdin.readline().split())
        need[to_num].append(from_num)
    target = int(sys.stdin.readline())

    stack = [target]
    sequence = [[target]]
    while True:
        temp = []
        for i in stack:
            temp += need[i]
        if len(temp) == 0:
            break
        temp = list(set(temp))
        stack = temp[::]
        sequence.append(temp)

    sequence.reverse()
    print(sequence)
    answer = 0

    for buildings in sequence:
        req_times = []
        for num in buildings:
            req_times.append(times[num - 1])
            times[num - 1] = 0
        answer += max(req_times)

    print(answer)



