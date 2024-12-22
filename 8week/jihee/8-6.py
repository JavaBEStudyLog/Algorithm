# 더 맵게 -> 우선순위 큐 heap

import heapq
def solution(scov, K):
    cnt = 0
    heapq.heapify(scov)
    while len(scov) > 1:
        m1 = heapq.heappop(scov)
        m2 = heapq.heappop(scov)
        if (m1 >= K) : return cnt
        new = m1 + m2*2
        heapq.heappush(scov, new)
        cnt += 1
        
    return cnt if scov[0] >= K else -1