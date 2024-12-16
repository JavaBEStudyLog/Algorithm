import math

def multiply(a, b):
    return (a * b) // math.gcd(a, b)

def solution(arr):
    result = arr[0]
    for num in arr[1:]:
        result = multiply(result, num)
    return result


