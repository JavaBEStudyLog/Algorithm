def solution(n):
    answer = []

    def hanoi(n, t1, t2, t3):
        if n == 1:
            answer.append([t1, t3])
            return
        hanoi(n - 1, t1, t3, t2)
        answer.append([t1, t3])
        hanoi(n - 1, t2, t1, t3)

    hanoi(n, 1, 2, 3)
    
    return answer
