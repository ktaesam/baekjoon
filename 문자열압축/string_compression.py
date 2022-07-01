# programmers
# level 2

def solution(s):
    answer = len(s)
    # 최대 len(s)//2+1 개 끊기
    for i in range(1, len(s) // 2 + 1):
        sentence = ''
        point = 0
        temp = s[:i]

        while point < len(s):
            cnt = 1

            # 중복되는 문자열일 경우
            while temp == s[point + i:point + i + i]:
                point += i
                cnt += 1

            # 문자열이 중복된 경우
            if cnt > 1:
                sentence += str(cnt)
                sentence += temp
            # 문자열이 중복되지 않은 경우
            else:
                sentence += temp

            # 다음 문자열 탐색
            point += i
            temp = s[point:point + i]

        # 문자열 압축의 최솟값
        answer = min(answer, len(sentence))

    return answer


