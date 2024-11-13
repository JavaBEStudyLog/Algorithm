import re
import sys


def solution(s):
    # 주어진 문자열의 집합들을 리스트로 변환
    s_tuples = [list(map(int, x.split(','))) for x in re.findall(r'\{([\d,]+)\}', s)]

    # 각 리스트의 원소 수
    count = []
    for i in range(len(s_tuples)):
        count.append(len(s_tuples[i]))

    answer = []

    for i in range(len(count)):
        # 가장 원소 수가 작은 리스트 부터 정답 리스트에 저장
        min_idx = count.index(min(count))
        # 원소 수가 가장 작은 리스트를 조회 후 값을 가장 큰값으로 변경 -> 추후 min 연산 시 배제됨
        count[min_idx] = sys.maxsize
        # 원소 수가 가장 작은 리스트
        s_tuple = s_tuples[min_idx]
        # 리스트에서 정답 리스트에 있는 요소들은 삭제
        for ans in answer:
            if ans in s_tuple:
                s_tuple.remove(ans)
        for s in s_tuple:
            answer.append(s)


    return answer

