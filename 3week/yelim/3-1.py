def solution(n):
    count = [0] * (n+1)
    count[0] = 1
    count[1] = 2

    for i in range(2,n):
        count[i] = count[i-2] + count[i-1]
    return count[n-1] % 1234567