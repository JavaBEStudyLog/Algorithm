import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix_count = 0
    while scoville[0] < K:
        if len(scoville) > 1:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new_scoville = first + 2 * second
            heapq.heappush(scoville, new_scoville)
            mix_count += 1
        else:
            return -1
    return mix_count
