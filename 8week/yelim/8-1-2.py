from datetime import datetime
import math

def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    parking_log = {}
    total_time = {}

    def time_to_minutes(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    for record in records:
        time, number, inout = record.split()
        time = time_to_minutes(time)
        if inout == "IN":
            parking_log[number] = time
        else:

            in_time = parking_log.pop(number)
            total_time[number] = total_time.get(number, 0) + (time - in_time)

    for number, in_time in parking_log.items():
        total_time[number] = total_time.get(number, 0) + (time_to_minutes("23:59") - in_time)

    answer = []
    for number in sorted(total_time.keys()):
        time = total_time[number]
        if time <= basic_time:
            fee = basic_fee
        else:
            extra_time = math.ceil((time - basic_time) / unit_time)
            fee = basic_fee + (extra_time * unit_fee)
        answer.append(fee)

    return answer

