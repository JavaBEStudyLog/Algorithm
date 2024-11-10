# 누적된 값이 최소인 경우를 찾아라 => 작은 수 * 큰 수 조합으로 만들어야 함

def solution(A,B):
    answer = 0
    
    # 하나는 오름차순, 하나는 내림차순으로 정렬
    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer