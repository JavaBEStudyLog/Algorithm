def solution(A, B):
    answer = []
    for i in range(0,len(A)):
        aa = []
        for k in range(0,len(B[0])):
            a = 0
            for j in range(0,len(B)):
                a += A[i][j]*B[j][k]
            aa.append(a)
        answer.append(aa)



    return answer
