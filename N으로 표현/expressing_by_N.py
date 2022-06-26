# programmers
# level 3

def solution(N, number):
    # 1번 계산
    result = dict()
    result[1] = [N]
    if N == number:
        return 1

    # 2번 ~ 8번 계산
    for n in range(2, 9):
        # 숫자 이어붙이는 경우
        num = int(str(N) * n)
        result[n] = [num]

        # n번 계산 하는 경우
        for i in range(1, n):
            set1 = result[i]
            set2 = result[n - i]
            # set1, set2의 원소들을 사칙연산 계산
            for a in set1:
                for b in set2:
                    result[n].append(a + b)
                    result[n].append(a - b)
                    result[n].append(b - a)
                    result[n].append(a * b)
                    if b != 0:
                        result[n].append(a // b)
                    if a != 0:
                        result[n].append(b // a)
            result[n] = list(set(result[n]))

            # 결과가 number라면 return
            if number in result[n]:
                return n

    # 9번 이상 필요한 경우 -1
    return -1