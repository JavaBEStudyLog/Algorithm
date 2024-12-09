from collections import Counter

def solution(want, number, discount):
    required = {w: n for w, n in zip(want, number)}
    total_days = len(discount)
    window_size = 10
    valid_days = 0

    for i in range(total_days - window_size + 1):
        current_window = discount[i:i + window_size]
        current_count = Counter(current_window)

        if all(current_count.get(item, 0) >= required[item] for item in required):
            valid_days += 1

    return valid_days

