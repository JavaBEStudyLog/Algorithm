def solution(people, limit):
    people.sort()
    
    answer = 0
    left_p, right_p = 0, len(people) - 1
    while left_p <= right_p:
        if (people[left_p] + people[right_p] <= limit):
            answer += 1
            left_p += 1
            right_p -= 1
        else:
            answer += 1
            right_p -= 1
    
    return answer
