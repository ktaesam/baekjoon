# gold 3

import sys
sys.stdin = open('input.txt')


from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, R = map(int, sys.stdin.readline().split())
    # 각 건물당 소요 시간
    build_times = [0] + list(map(int, sys.stdin.readline().split()))

    # 필요한 선행 건물 갯수
    need = [0 for _ in range(N + 1)]
    # 건설 규칙
    rules = [[] for _ in range(N + 1)]
    # 최소 소요 시간
    times = [0 for _ in range(N + 1)]

    # 건설 규칙 저장
    for r in range(R):
        from_num, to_num = map(int, sys.stdin.readline().split())
        rules[from_num].append(to_num)
        need[to_num] += 1
    # 목표 건물
    target = int(sys.stdin.readline())

    # 선행 건물이 없으면 큐에 저장
    queue = deque()
    for i in range(1, N + 1):
        if need[i] == 0:
            queue.append(i)
            times[i] = build_times[i]

    # 각 건물당 최소 소요시간 저장
    while queue:
        now = queue.popleft()
        for i in rules[now]:
            need[i] -= 1
            times[i] = max(times[now] + build_times[i], times[i])
            if need[i] == 0:
                queue.append(i)

    answer = times[target]

    print(answer)

