# 후보키
# 모든 속성의 조합 확인 -> 유일성 확인 -> 최소성 확인

from itertools import combinations

def solution(relation):
    r = len(relation)
    c = len(relation[0])
    
# 모든 속성 조합
    all_case = []
    for i in range(1, c + 1):
        all_case.extend(combinations(range(c), i))
    
# 유일성 확인
    unique = []
    for case in all_case:
# 조합에 해당하는 열의 값의 집합
        tmp = [tuple(item[idx] for idx in case) for item in relation]
        # 각 조합의 중복 체크
        if len(set(tmp)) == r:
            unique.append(case)
            
    # 최소성 확인        
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
# 두 조합의 교집합의 길이와 첫 조합의 길이가 같으면 두 번째 조합은 제거
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                answer.discard(unique[j])
                      
    return len(answer)