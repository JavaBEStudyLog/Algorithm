# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    
    ap = [0] * (n+2)
    ap[1] = 1
    ap[2] = 2
    
    if n <= 2:
        return ap[n] % 1234567
    else:
        for i in range(3, n+1):
            ap[i] = ap[i-1] + ap[i-2]
        return ap[n] % 1234567