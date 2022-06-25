# gold 1

import sys, math
sys.stdin = open('input.txt')

# 최솟값, 최댓값
min_num, max_num = map(int, sys.stdin.readline().split())

num_list = [1] * (max_num - min_num + 1)

maximal = math.floor(math.sqrt(max_num))
# 제곱수의 배수일 경우 0
for i in range(2, maximal + 1):
    start = (min_num // (i ** 2)) * (i ** 2)
    idx = start
    if idx < min_num:
        idx += i ** 2
    while idx <= max_num:
        num_list[idx - min_num] = 0
        idx += i ** 2

# 제곱수의 배수가 아닌 수의 갯수
answer = sum(num_list)

print(answer)
