# 귤 고르기
# 서로 다른 종류를 최소화,,, -> counter

from collections import Counter
def solution(k, tangerine):
    cnt = 0
    a = Counter(tangerine)
    
    for item, count in a.most_common():
        k -= count
        cnt += 1
        if k <= 0 : break
    
    
    return cnt

