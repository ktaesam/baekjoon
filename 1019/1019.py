# gold 1

import sys

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):

    pages = sys.stdin.readline().strip()
    page = [0] * 10

    for i in range(len(pages)):
        # 매 자리수 별로 front, mid, end로 구분
        if pages[:len(pages)-i-1]:
            front = int(pages[:len(pages)-i-1])
        else:
            front = -1

        mid = int(pages[len(pages)-i-1])

        if pages[len(pages)-i:]:
            end = int(pages[len(pages)-i:])
        else:
            end = -1


        # front 만큼 i 자리수 0 ~ 9 반복
        if front != -1:
            for j in range(10):
                page[j] += front * (10 ** i)

        # i 자리수 0 ~ mid-1 반복
        for j in range(mid):
            page[j] += 10 ** i

        # i 자리수 mid, end+1 반복
        if end != -1:
            page[mid] += end + 1
        else:
            page[mid] += 1

        page[0] -= 10 ** i
        
    answer = ' '.join(map(str, page))
    print(answer)
