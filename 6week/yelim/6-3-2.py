def solution(dirs):


    walk_list = []
    start_location = [0,0]
    now_location = [0,0]
    for c in dirs:
        if c == 'U' and start_location[1] < 5:
            now_location = [start_location[0],start_location[1] + 1]

        elif c == 'L' and start_location[0] > -5:
            now_location = [start_location[0] - 1, start_location[1]]

        elif c == 'R' and start_location[0] < 5:
            now_location = [start_location[0] + 1, start_location[1]]

        elif c == 'D'and start_location[1] > -5:
            now_location = [start_location[0], start_location[1] - 1]


        if ([start_location,now_location] not in walk_list) and ([now_location,start_location] not in walk_list) \
                and (now_location != start_location) :
            walk_list.append([start_location,now_location])

        start_location = now_location

    return len(walk_list)
