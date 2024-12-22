# 요격 시스템

def solution(targets):
    answer = 0
    bound = 0

    for s, e in sorted(targets):
        if bound > s:
            bound = min(bound, e)
        else:
            bound = e
            answer += 1

    return answer