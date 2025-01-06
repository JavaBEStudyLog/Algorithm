from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    len1 = len2 = len(queue1)
    sum1, sum2 = sum(queue1), sum(queue2)

    answer = 0
    while sum1 != sum2:
        if not len1 or not len2 or answer > 2*(len1+len2):
            answer = -1
            break

        if sum1 < sum2:
            answer += 1
            len1, len2 = len1+1, len2-1
            sum1, sum2 = sum1+queue2[0], sum2-queue2[0]
            queue1.append(queue2.popleft())
        else:
            answer += 1
            len1, len2 = len1-1, len2+1
            sum1, sum2 = sum1-queue1[0], sum2+queue1[0]
            queue2.append(queue1.popleft())

    return answer
