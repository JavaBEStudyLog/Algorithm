def solution(storey):
    answer = 0  # 마법의 돌의 최소 개수를 저장할 변수
    while storey > 0:
        digit = storey % 10  # 현재 층의 일의 자리 숫자 추출
        storey //= 10  # 현재 층을 10으로 나누어 다음 자릿수로 이동

        if digit < 5:  # 5보다 작은 경우 내림
            answer += digit
        elif digit == 5:
            # 다음 자리가 5보다 작을 경우 내림
            if storey % 10 < 5:
                answer += digit  # 5에서 내리기
            else:
                answer += 10 - digit  # 올림이 더 유리함
                storey += 1  # 올리기 위해 다음 자릿수에 1을 더함
        else:  # 5보다 큰 경우 올림
            answer += 10 - digit  # 올리기 위한 버튼 수
            storey += 1  # 올림 처리

    return answer  # 최소 마법의 돌 개수를 반환
