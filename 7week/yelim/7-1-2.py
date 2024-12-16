def solution(plans):
    def time_to_sec(time_str):
        hour, minute = tuple(map(int,time_str.split(':')))
        return hour * 60 + minute
    plans = list(map(lambda x:[x[0],time_to_sec(x[1]),int(x[2])],plans))
    plans.sort(key=lambda x: x[1])

    answer = []
    cur ,cur_time = 0, plans[0][1]
    while plans:
        if cur == len(plans) - 1 or cur_time + plans[cur][2] <= plans[cur+1][1]:
            answer.append(plans[cur][0])
            cur_time = cur_time + plans[cur][2]
            plans.pop(cur)
            if len(plans) > 0 and cur == 0:
                cur_time = plans[cur][1]
            elif cur == len(plans) or cur_time < plans[cur][1]:
                cur -= 1
        else:
            plans[cur][2] -= plans[cur+1][1] - cur_time
            cur_time = plans[cur+1][1]
            cur += 1

    return answer
