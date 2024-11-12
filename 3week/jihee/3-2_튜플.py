# https://school.programmers.co.kr/learn/courses/30/lessons/64065

# 빈도순으로 정렬 => n이라는 숫자가 k번 나왔다 => 딕셔너리에 저장
def solution(s):
    num_count = dict()
    
    s=s.replace("{","").replace("}","").split(",")
    
    for i in s:
        i = int(i)
        
        if i in num_count:
            num_count[i] += 1
        else:
            num_count[i] = 1
            
    # value(num_count[x])를 기준으로 내림차순 정렬
    answer = sorted(num_count, key=lambda x:num_count[x], reverse=True)

    return answer
