# 공백 이후에 나오는 문자만 대문자로, 그 외 문자는 소문자로 바꿔서 출력
# 모두 소문자로 변환한 뒤, 공백 다음것만 대문자로 바꿔주기

def solution(s):
    s = s.lower()
    s = s.split(' ')
    answer = []
    
    for i in s :
        i = i[0].upper() + i[1:]
        answer.append(i)
    return ' '.join(answer)


# 런타임 에러  =>  대문자로 바꾸는 부분 내장함수 사용하면 해결 가능 i = i.capitalize()