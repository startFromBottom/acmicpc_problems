"""

problem link : https://www.acmicpc.net/problem/4963

"""

from typing import List


def solution(M: int, N: int, matrix: List[List[int]]) -> int:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    def dfs(x: int, y: int):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and \
                    matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and matrix[i][j] == 1:
                dfs(i, j)
                cnt += 1

    return cnt


if __name__ == "__main__":
    while True:
        M, N = map(int, input().split())
        if (M, N) == (0, 0):
            break
        matrix = [list(map(int, input().split())) for _ in range(N)]
        print(solution(M, N, matrix))
