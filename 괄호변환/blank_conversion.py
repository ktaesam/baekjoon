# programmers
# level 2

def solution(p):
    # 빈 문자열인 경우 그대로 반환
    if p == '':
        return ''
    
    # 균형잡힌 괄호 문자열 u,v로 분리
    # 균형잡힌 = 괄호의 쌍을 만족하는
    blank_open = 0
    blank_close = 0
    for i in range(len(p)):
        
        if p[i] == '(':
            blank_open += 1
        elif p[i] == ')':
            blank_close += 1
        
        if blank_open == blank_close:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    
    # u가 올바른 괄호 문자열임을 확인
    # 올바른 = 괄호쌍의 순서를 만족하는
    condition = 0
    for i in range(len(u)):
        if u[i] == '(':
            condition += 1
        elif u[i] == ')':
            condition -= 1
        
        # u가 올바른 괄호 문자열이 아니라면
        if condition < 0:
            # u의 첫번째, 마지막 문자를 제거
            # 나머지 문자열의 괄호 변경
            u = u[1:-1]
            new_u = ''
            for j in range(len(u)):
                if u[j] == '(':
                    new_u += ')'
                elif u[j] == ')':
                    new_u += '('
            # '(' + v에 대해 재귀적으로 수행한 결과 + ')' + 새로 만든 u
            return '(' + solution(v) + ')' + new_u
    
    # u가 올바른 괄호 문자열이라면
    # u + v에 대해 재귀적으로 수행한 결과
    return u + solution(v)