# programmers
# level2

import math

def solution(w,h):
    # gcd(w,h)개의 독립된 삭제칸 형성
    divisor = math.gcd(w,h)
    
    # 독립된 부분에서 짧은 변, 긴 변
    short = min(w // divisor, h // divisor)
    long = max(w // divisor, h // divisor)
    
    # 독립된 부분에서 삭제되는 칸의 개수
    cells = short + long - 1
    
    # 온전한 정사각형의 개수
    answer = w * h
    answer -= cells * divisor
    
    
    return answer