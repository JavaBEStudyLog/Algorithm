# 연속되 부분 수열의 합
# 합이 k가 되는 부분 수열 -> 여러 개인 경우 길이가 짧은 수열의 인덱스를 반환

def solution(seq, k):
    total, limit_len, idx = 0, 0, -1
    if k in seq : return [seq.index(k), seq.index(k)]

    for i in range(len(seq)-1, -1, -1):
        total += seq[i]
        while total > k :
            total -= seq.pop()

        if total == k : 
            if limit_len and len(seq)-1-i > limit_len : return [idx, idx+limit_len]
            else : limit_len = len(seq) - 1 - i; idx = i

    return [idx, idx+limit_len]