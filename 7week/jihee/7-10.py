# 파일명 정렬
# head, number, tail로 구분해서 정렬

def solution(files):
    answer = []
    
    li = list()
    for i in files:
        head = ""
        j = 0
        while (not i[j].isnumeric()):
            head += i[j]
            j += 1
        
        number = ""
        while (i[j].isnumeric()):
            number += i[j]
            j += 1
            if (j >= len(i)):
                break

        tail = i[j : ]
    
        word = [head, number, tail]

        li.append(word)

    li.sort(key = lambda x: int(x[1]))
    li.sort(key = lambda x: x[0].lower())

    for i in li:
        word = ''
        for j in i:
            word += j
        answer.append(word)
    
    return answer