from collections import Counter

def solution(k, tangerine):
    tangerine_count = Counter(tangerine)
    tangerines = sorted(tangerine_count.values())

    k = len(tangerine) - k
    while k > 0:
        if k >= tangerines[0]:
            k -= tangerines[0]
            del tangerines[0]
        else:
            k = 0 
    answer = len(tangerines)
    return answer
