def solution(brown, yellow):
    height = 1
    width = yellow 
    
    while True:
        if (height * 2 + ( width  + 2 ) * 2) == brown:
            return [width+2,height+2]
            break

        height+=1
        width = yellow / height 
