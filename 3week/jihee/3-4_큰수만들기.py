def solution(number, k):
    # 자릿수 : len(number) - k
    # 제일 큰 수부터 차례대로 나열
    
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    stack = stack[:len(number) - k]
    
    answer = ''.join(stack)
    return answer