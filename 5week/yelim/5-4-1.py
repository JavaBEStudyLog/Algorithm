import math

def solution(n, k):
    number = list(range(1, n + 1))
    result = []
    
    for i in range(n, 0, -1):
        factorial = math.factorial(i - 1)
        index = (k - 1) // factorial
        result.append(number.pop(index))
        k -= index * factorial
    
    return result
