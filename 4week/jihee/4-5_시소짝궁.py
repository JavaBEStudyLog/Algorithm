from collections import Counter

def solution(weights):
    counter = Counter(weights)
    answer = 0

    for c in counter:
        if counter[c] > 0:
            # 자기 자신과 동일 -> 같은 거리에 앉아야함
            answer += counter[c] * (counter[c] - 1) // 2 # nC2 n!/2!(n - 2)!
            # 두 명이 앉는 경우의 수 -> 다른 거리에 앉아야함
            answer += counter[c] * counter[c * 4 / 3] # 4m & 3m
            answer += counter[c] * counter[c * 4 / 2] # 4m & 2m
            answer += counter[c] * counter[c * 3 / 2] # 3m & 2m

    return answer
