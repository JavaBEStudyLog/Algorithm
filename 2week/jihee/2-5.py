# 문자열에서 0을 제거
# 남은 1의 개수를 이진법으로 변환
# 1이 될때까지 반복!

def solution(s):
    delete_cnt = 0
    change_cnt = 0
    
    while s != '1' :
        delete_cnt += s.count("0") # 0의 개수 누적
        
        cnt_1 = s.count("1") # 1의 개수
        s = bin(cnt_1)[2:] # bin의 반환값 형태가 0b~~~ 형태이기 때문에 2번 인덱스부터 저장
        
        change_cnt += 1 # 이진 변환 횟수 증가
    
    return [change_cnt, delete_cnt]