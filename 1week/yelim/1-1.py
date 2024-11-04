def solution(diffs, times, limit):
    answer = 0

    max_diff = max(diffs)

    def cal(level):
        time = 0
        for idx, diff in enumerate(diffs):
            if diff <= level:
                time += times[idx]
            else:
                time += (diff-level) * (times[idx]+times[idx-1]) + times[idx]

        return time

    st, en = 1, max_diff
    while st < en:
        level = (st+en)//2

        if cal(level) > limit:
            st = level + 1
        else:
            en = level

    return en
