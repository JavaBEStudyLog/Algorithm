def solution(n):
    answer = [[0] * (i + 1) for i in range(n)]
    count = 1
    answer[0][0] = count
    current = [0, 0]
    ways = 'down'
    while count < n * (n + 1) // 2:  # count < 로 수정
        if ways == 'down':
            for i in range(current[0] + 1, n):
                current[0] += 1
                count += 1
                answer[current[0]][current[1]] = count
            ways = 'stay'
        elif ways == 'stay':
            for i in range(current[1] + 1, n):
                current[1] += 1
                count += 1
                answer[current[0]][current[1]] = count
            ways = 'up'
        elif ways == 'up':
            for i in range(current[0] - 1, 0, -1):
                current[0] -= 1
                current[1] -= 1
                count += 1
                answer[current[0]][current[1]] = count
            ways = 'down'

    # 마지막 숫자 추가
    if count == n * (n + 1) // 2:
        answer[current[0]][current[1]] = count

    return sum(answer,[] )
