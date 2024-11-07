def solution(s):
    stack = []
    for i in s:
        # 스택이 비어있는데 )가 들어온 경우 => false
        if len(stack) == 0 and i == ')':
            return False
        
        # ( 만 스택에 넣고, ) 가 들어오면 스택에서 제거
        if i == '(':
            stack.append('(')
        
        if i == ')' and stack[-1] == '(':
            stack.pop()
            
    return True if len(stack) == 0 else False