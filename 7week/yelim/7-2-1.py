def solution(n, words):
    history = [words[0]]

    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            return [(i % n) + 1,(i // n) + 1]
        
        if words[i] in history:
            return [(i % n) + 1, (i // n) + 1]
        
        history.append(words[i])
    return [0, 0]
