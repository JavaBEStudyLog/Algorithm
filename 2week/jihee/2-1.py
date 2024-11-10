def solution(s):
    number = list(map(int, s.split()))
    return str(min(number)) + " " +str(max(number))