def solution(s):
    answer = ''
    # 첫 문자인지 체크
    check = 1

    for i in range(len(s)):
        #공백이면 공백 추가, 공백이후엔 대문자가 와야하므로 check=1
        if s[i] == " ":
            answer+= " "
            check = 1
        # 공백이 아니고, 첫무문자 일경우 대문자로 추가
        # 이후 소문자로 추가해야함으로 check를 0으로 설정
        elif s[i] != " " and check == 1:
            answer += s[i].upper()
            check = 0
        # 소문자 위치라면 소문자로 변환하여 추가
        elif check == 0:
            answer += s[i].lower()
    return answer