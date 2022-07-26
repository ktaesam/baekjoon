import sys

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    wave = sys.stdin.readline()
    flag = 1

    # 전파 분석
    while len(wave):

        # 01 로 시작하는 경우
        if wave.startswith('01'):
            wave = wave[2:]

        # 100 으로 시작하는 경우
        elif wave.startswith('100'):
            wave = wave[3:]
            wave = wave.lstrip('0')
            if len(wave) == 0:
                flag = 0
                break
            else:
                if wave.startswith('10'):
                    wave = wave.lstrip('1')
                else:
                    wave = wave.lstrip('1')
                    if wave.startswith('00'):
                        wave = '1' + wave

        # 그 외의 경우에 패턴x
        else:
            flag = 0
            break

    if flag == 1:
        print('YES')
    else:
        print('NO')