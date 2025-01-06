def solution(targets):
    answer = 1
    targets = sorted(targets, key=lambda x: x[1])
    maxhit = targets[0][1] - 0.5
    for target in targets:
        if target[0] > maxhit:
            maxhit = target[1] - 0.5
            answer += 1
    return answer
