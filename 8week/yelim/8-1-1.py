def solution(n):
    def dfs(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if not (cols[col] or diag1[row + col] or diag2[row - col + n - 1]):
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                count += dfs(row + 1)
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False
        return count

    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    return dfs(0)
