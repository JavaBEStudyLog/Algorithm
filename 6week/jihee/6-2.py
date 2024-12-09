
# 그리디

def solution(people, limit):
    answer = 0
    end = len(people)
    people.sort()
    for i in range(len(people)//2):
        while(end > i + 1):
            end -= 1
            if people[i] + people[end] <= limit:
                answer += 1
                break
    answer += (len(people) - 2 * (answer))
    return answer