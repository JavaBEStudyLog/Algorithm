# 짝지어 제거하기 -> 스택 이용. 
# 이전 == 현재 pop 반복 -> 남아있으면 0, 없으면 1

def solution(s):
    tmp = []
    for i in s:
        if len(tmp) == 0:
            tmp.append(i)
        elif tmp[-1] == i:
            tmp.pop()
        else:
            tmp.append(i)
    if len(tmp) == 0:
        return 1
    return 0