"""

problem link : https://www.acmicpc.net/problem/2178

"""

from typing import List
from collections import deque


def solution(N: int, M: int, matrix: List[List[int]]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dist = [[0 for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0)])
    dist[0][0] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if dist[nx][ny] == 0 and matrix[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist[N - 1][M - 1]


if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    print(solution(N, M, matrix))
