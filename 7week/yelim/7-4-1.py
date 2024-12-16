def solution(citations):
    citations.sort(reverse=True)
    idx = 0
    
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            idx = i + 1
        else:
            break
    
    return idx
