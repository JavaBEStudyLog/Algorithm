# 카펫 크기

def solution(brown, yellow):
    i = 1
    while True:
        y_h = i
        y_w = yellow / y_h

        if brown == (y_h * 2) + ((y_w + 2) * 2):
            answer = [round(y_w + 2), (y_h + 2)]
            break
        i += 1

    return answer