def solution(diffs, times, limit):
    
    answer = 0
    
    min_diff = min(diffs)
    max_diff = max(diffs)
    
    while (True):
        # 임의로 숙련도 설정
        level = (max_diff + min_diff) // 2
        
        total_time = 0
        time_prev = 0
        
        for i in range(len(diffs)):
            time_cur = times[i]
            diff = diffs[i]
            
            if(diff <= level) :
                total_time += time_cur
            else:
                total_time += (time_cur + time_prev) * (diff-level) + time_cur
            time_prev = time_cur
            
        
        # 제한시간 내에 못 푼 경우, 숙련도를 높여서 다시 계산
        if(total_time > limit):
            min_diff = level+1
        # 제한시간 내에 푼 경우, 숙련도를 낮춰서 다시 계산
        # 지금 숙련도가 정답일 수 있으니 level에 저장해두기
        else:
            max_diff = level-1
            answer = level
    
    return answer