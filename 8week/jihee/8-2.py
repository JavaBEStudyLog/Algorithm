# 주차 요금 계산

import math
from datetime import datetime
def solution(fees, records):
    answer, nums = [], {}
    for record in records:
        time, num, state = record.split(" ")
        if num in nums.keys(): nums[num] = nums[num]+[time]
        else : nums[num] = [time]
    nums = {k:v for k,v in sorted(nums.items())}

    for lst in nums.values():
        minutes = 0
        if len(lst)%2 == 1: lst.append('23:59')
        for i in range(0,len(lst),2):
            time_diff = datetime.strptime(lst[i+1], '%H:%M') - datetime.strptime(lst[i], '%H:%M')
            minutes += time_diff.total_seconds() // 60
        if minutes <= fees[0] : answer.append(fees[1])
        else : 
            price = fees[1] + (math.ceil((minutes - fees[0])/fees[2]))*fees[3]
            answer.append(price)

    return answer