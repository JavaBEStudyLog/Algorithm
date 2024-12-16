# N개의 최소공배수 -> 배수 중 공통이 되는 가장 작은 숫자 찾기

import math
def solution(arr):
    
    while len(arr) >= 2:
        a, b = arr[0], arr[1]
        arr.append((a*b) // math.gcd(a,b))
        arr = arr[2:]
        
    return arr[0]