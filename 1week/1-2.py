def solution(points, routes):
    # 포인트의 개수
    n = len(points)
    # 로봇의 개수
    x = len(routes)
    
    # 포인트 좌표를 딕셔너리에 저장
    point_dict = {i + 1: (points[i][0], points[i][1]) for i in range(n)}
    
    # 시간에 따른 로봇 위치 기록
    time_positions = {}  # 일반 딕셔너리로 변경

    # 각 로봇의 경로를 시뮬레이션
    for robot_id in range(x):
        path = routes[robot_id]
        current_pos = point_dict[path[0]]  # 로봇의 시작점
        time = 0

        # 각 로봇의 경로를 따라 이동
        for j in range(len(path) - 1):
            start_coords = point_dict[path[j]]
            end_coords = point_dict[path[j + 1]]
            
            r1, c1 = start_coords
            r2, c2 = end_coords
            
            # 현재 위치 업데이트
            while (r1, c1) != (r2, c2):
                if time not in time_positions:
                    time_positions[time] = []  # 수동으로 빈 리스트 생성
                time_positions[time].append((r1, c1))
                
                if r1 < r2:
                    r1 += 1
                elif r1 > r2:
                    r1 -= 1
                elif c1 < c2:
                    c1 += 1
                elif c1 > c2:
                    c1 -= 1
                
                time += 1
        
        # 마지막 위치를 기록 (도착 지점)
        if time not in time_positions:
            time_positions[time] = []  # 수동으로 빈 리스트 생성
        time_positions[time].append((r1, c1))

    # 충돌 횟수 카운트
    collision_count = 0
    for positions in time_positions.values():
        position_counter = {}  # 일반 딕셔너리로 변경
        
        # 각 시간대의 위치를 카운트
        for pos in positions:
            if pos in position_counter:
                position_counter[pos] += 1
            else:
                position_counter[pos] = 1
        
        # 충돌 발생 확인
        for count in position_counter.values():
            if count > 1:
                # 같은 위치에 여러 로봇이 있으면 충돌
                collision_count += count * (count - 1) // 2  # 조합 수로 충돌 횟수 계산

    return collision_count