import heapq

def time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def solution(book_time):
    bookings = [(time_to_minutes(start), time_to_minutes(end) + 10) for start, end in book_time]
    bookings.sort()

    rooms = []
    for start, end in bookings:
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)