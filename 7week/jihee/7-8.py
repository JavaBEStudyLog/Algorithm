# 주식 가격
# 주식 가격이 하락할 때를 파악

def solution(prices):
    answer = [0] * len(prices) 
    for i, p in enumerate(prices):
        for j in range(i+1 , len(prices)):
            if p <= prices[j]:
                answer[i] += 1
            #price drops 
            else: 
                answer[i] = j - i
                break 
    return answer