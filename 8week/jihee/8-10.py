# n^2 배열 자르기

def solution(n, left, right):
    result = []

    for i in range(left, right+1):
        y, x = i//n, i%n
        value = max(y,x) + 1
        result.append(value)

    return result