def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        while stack and prices[i] < prices[stack[-1]]:
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx
        stack.append(i)
    
    while stack:
        prev_idx = stack.pop()
        answer[prev_idx] = n - 1 - prev_idx
    
    return answer
