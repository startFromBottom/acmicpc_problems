"""

problem link : https://www.acmicpc.net/problem/1012

"""
from collections import deque


def solution():
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(a: int, b: int):
        q = deque([(a, b)])
        matrix[a][b] = -1
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and \
                        matrix[nx][ny] == 1:
                    matrix[nx][ny] = -1
                    q.append((nx, ny))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                cnt += 1
                bfs(i, j)

    return cnt


if __name__ == "__main__":

    T = int(input())

    for _ in range(T):
        M, N, K = map(int, input().split())
        matrix = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            y, x = map(int, input().split())
            matrix[x][y] = 1
        print(solution())
