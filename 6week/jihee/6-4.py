# 완전 탐색

from itertools import product
def solution(word):
    l1 = []
    words = ['A','E','I','O','U']
    for i in range(1,6):
        for j in list(product(words, repeat=i)):
            l1.append(''.join(j))
    l1.sort()
    return l1.index(word)+1