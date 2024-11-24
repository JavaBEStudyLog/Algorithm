from collections import deque


def solution(maps):
    rows, cols = len(maps), len(maps[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(start, lever_needed):
        queue = deque([start])
        visited = [[[False, False] for _ in range(cols)] for _ in range(rows)]
        visited[start[0]][start[1]][lever_needed] = True
        time = 0

        while queue:
            for _ in range(len(queue)):
                x, y, lever_status = queue.popleft()

                if maps[x][y] == 'E' and lever_status == 1:
                    return time

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols:
                        if maps[nx][ny] != 'X' and not visited[nx][ny][lever_status]:
                            if maps[nx][ny] == 'L' and lever_status == 0:
                                visited[nx][ny][1] = True
                                queue.append((nx, ny, 1))
                            else:
                                visited[nx][ny][lever_status] = True
                                queue.append((nx, ny, lever_status))
            time += 1

        return -1

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S':
                start = (i, j, 0)
                break

    return bfs(start, 0)