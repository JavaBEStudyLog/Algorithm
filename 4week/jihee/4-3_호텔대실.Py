def solution(book_time):
    # 시간을 분 단위로 변환하는 함수
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes

    # 예약 시간을 분 단위로 변환하고 종료 시간에 10분 추가
    events = []
    for start, end in book_time:
        start_minutes = time_to_minutes(start)
        end_minutes = time_to_minutes(end) + 10  # 청소 시간 10분 추가
        events.append((start_minutes, 'start'))
        events.append((end_minutes, 'end'))

    # 이벤트를 시간 순으로 정렬, 동일 시간일 경우 'end'가 'start'보다 우선
    # x[1] == 'start' 가 True이면 1, False면 0 => 정렬하면 0, 즉 False가 먼저 정렬되므로 end를 우선시함
    events.sort(key=lambda x: (x[0], x[1] == 'start'))

    # 현재 사용 중인 객실 수와 최대 객실 수 추적
    current_rooms = 0
    max_rooms = 0
    for event in events:
        if event[1] == 'start':
            current_rooms += 1
            max_rooms = max(max_rooms, current_rooms)
        else:
            current_rooms -= 1

    return max_rooms
