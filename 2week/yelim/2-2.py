def solution(s):
    SList = []
    for ele in s:
        if ele == '(':
            SList.append(SList)
        elif ele == ')':
            if len(SList) == 0:
                return False
            else:
                SList.pop(len(SList)-1)
    return True