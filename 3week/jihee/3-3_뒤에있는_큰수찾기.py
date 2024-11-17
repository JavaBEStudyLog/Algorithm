def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [] # numbers의 인덱스를 저장하기 위한 스택
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i] 
            # stack.pop()을 해주기 때문에 한번 수행하면 stack은 빈 상태가 됨 
            # => while문을 빠져나가서 append 수행
        stack.append(i)
    return answer

numbers = [2,3,3,5]
print(solution(numbers))