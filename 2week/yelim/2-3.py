def solution(s):
    count = 0
    removeCount = 0

    while len(s) != 1:
        count += 1
        tmpS = len(s)

        s = s.replace("0","")
        removeCount += tmpS - len(s)

        s = str(format(len(s),'b'))

    return [count, removeCount]