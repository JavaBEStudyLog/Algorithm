from math import gcd
from functools import reduce

def solution(arrayA, arrayB):

    def find_gcd(arr):
        return reduce(gcd, arr)

    def check_gcd(g, arr):
        for num in arr:
            if num % g == 0:
                return False
        return True

    gcd_a = find_gcd(arrayA)
    gcd_b = find_gcd(arrayB)

    result = 0

    if check_gcd(gcd_a, arrayB):
        result = max(result, gcd_a)

    if check_gcd(gcd_b, arrayA):
        result = max(result, gcd_b)

    return result if result != 0 else 0