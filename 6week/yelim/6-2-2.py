def solution(word):
    index = [781, 156, 31, 6, 1]
    alphabet = ['A', 'E', 'I', 'O', 'U']
    rank = 0
    for i, char in enumerate(word):
        rank += alphabet.index(char) * index[i] + 1

    return rank
