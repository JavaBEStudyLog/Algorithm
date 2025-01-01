# 점 찍기

def solution(k, d):
    answer = 0
    d_2 = d ** 2

    x = 0
    while x <= d:
        y = 0
        max_v = int((d_2 - x**2) **(0.5))
        rest = max_v % k
        answer += (max_v - rest) / k + 1
        x += k


    return answer