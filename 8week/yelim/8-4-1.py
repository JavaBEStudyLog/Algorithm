def solution(sequence, k):
    start, end = 0, 0
    current_sum = 0
    best_length = float('inf')

    while end < len(sequence):
        current_sum += sequence[end]
        while current_sum >= k and start <= end:
            if current_sum == k:
                if end - start + 1 < best_length:
                    best_length = end - start + 1
                    answer = [start, end]
            current_sum -= sequence[start]
            start += 1
        end += 1

    return answer
