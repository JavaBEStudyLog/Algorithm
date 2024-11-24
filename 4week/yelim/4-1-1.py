def calculate_solve_time(level, diffs, times):
    total = 0

    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]

        if diff <= level:
            total += time_cur
        else:
            time_prev = times[i - 1]
            total += (time_prev + time_cur) * (diff - level) + time_cur

    return total


def solution(diffs, times, limit):
    min_level, max_level = 1, max(diffs)
    min_time = pow(10, 15)

    while min_level <= max_level:
        level = (min_level + max_level) // 2
        calculated_time = calculate_solve_time(level, diffs, times)

        if calculated_time > limit:
            min_level = level + 1
        else:
            max_level = level - 1
            min_time = min(min_time, level)

    return min_time