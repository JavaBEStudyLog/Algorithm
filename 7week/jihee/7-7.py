# H-index

def solution(citations):
    result = 0
    citations.sort(reverse=True)
    for idx, i in enumerate(citations, start = 1):
        result = max(result, min(i, idx))
    return result