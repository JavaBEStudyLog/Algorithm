from itertools import combinations

def solution(relation):
    rows = len(relation)
    cols = len(relation[0])
    combinations_list = []
    candidate = []

    for i in range(1, cols + 1):
        combinations_list.extend(combinations(range(cols), i))

    for comb in combinations_list:
        temp = [tuple(row[c] for c in comb) for row in relation]
        if len(set(temp)) == rows:
            duplicated = True
            for key in candidate:
                if set(key).issubset(set(comb)):
                    duplicated = False
                    break
            if duplicated:
                candidate.append(comb)

    return len(candidate)
