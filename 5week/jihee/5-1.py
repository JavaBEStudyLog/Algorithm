def solution(n):

    before, after, total = 0, 1, 0
    for i in range(n-1):
        total = before + after
        before = after
        after = total

    return total % 1234567
