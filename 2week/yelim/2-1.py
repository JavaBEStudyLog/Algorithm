def solution(s):
    str_list = list(map(int,s.split()))

    maxValue = str_list[0]
    minValue = str_list[0]

    for ele in str_list:
        if ele > maxValue:
            maxValue = ele
        if ele < minValue:
            minValue = ele
    answer = str(minValue) + ' ' + str(maxValue)

    return answer