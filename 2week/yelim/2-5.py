def solution(A, B):
    answer = 0
    B.sort()
    A.sort()
    B.reverse()

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer