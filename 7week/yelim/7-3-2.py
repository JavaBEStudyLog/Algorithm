def solution(s):
    answer = len(s)
    length = 1
    copy_s = s

    while length < answer - 1:
        tmp = ""
        count = 0
        tmp_len = 0
        while True:
            if tmp == None:
                pass
            else:
                if tmp == s[:length]:
                    count += 1
                else:
                    tmp_len += len(tmp) + len(str(count+1)) if count else len(tmp)
                    count = 0
            if not s:
                break
            tmp = s[:length]
            s = s[length:]
        if tmp_len < answer:
            answer = tmp_len
        s = copy_s
        length += 1
    return answer
