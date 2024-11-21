import math

def solution(arrayA, arrayB):
    cc, yc = 0, 0
    
    for i in range(len(arrayA)):
        cc = math.gcd(cc, arrayA[i])
    
    for j in range(len(arrayB)):
        yc = math.gcd(yc, arrayB[j])
        
    for k in range(len(arrayA)):
        if arrayA[k] % yc == 0:
            yc = 1
        if arrayB[k] % cc == 0:
            cc = 1
    
    if cc == 1 and yc == 1:
        return 0
    else :
        return max(cc, yc) 