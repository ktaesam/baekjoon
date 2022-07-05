# programmers
# level 2

from collections import defaultdict

def solution(records):
    answer = []
    # 유저 id와 이름을 저장
    temp = []
    names = defaultdict()
    
    for record in records:
        info = record.split()

        # 입장시 해당 문구를 answer에 추가하고
        # names에 id와 이름 등록
        if info[0] == 'Enter':
            names[info[1]] = info[2]
            answer.append('님이 들어왔습니다.')
            temp.append(info[1])

        # 퇴장시 해당 문구를 answer에 추가
        elif info[0] == 'Leave':
            answer.append('님이 나갔습니다.')
            temp.append(info[1])

        # 이름 변경시 names에 이름 변경
        elif info[0] == 'Change':
            names[info[1]] = info[2]
            
    # temp를 이용하여 answer에 해당 id의 이름 추가
    for i in range(len(answer)):
        answer[i] = names[temp[i]] + answer[i]
        
    return answer