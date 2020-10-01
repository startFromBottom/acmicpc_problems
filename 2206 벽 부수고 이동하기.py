"""

problem link : https://www.acmicpc.net/problem/2206

"""


from typing import List
from collections import deque


def solution(N: int, M: int, matrix: List[List[int]]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # [a, b] -> a : 벽을 뚫지 않았을 때 거리 정보, b : 벽을 1번 뚫었을 때의 거리 정보
    dist = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque([(0, 0, 0)])
    dist[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                # 벽이 아닐 때(이전에 벽 만난 적 없거나, 1번 만난 경우 모두 포함)
                if matrix[nx][ny] == 0 and dist[nx][ny][z] == 0:
                    dist[nx][ny][z] = dist[x][y][z] + 1
                    q.append((nx, ny, z))
                # 처음으로 벽을 만남
                if z == 0 and matrix[nx][ny] == 1 and dist[nx][ny][1] == 0:
                    dist[nx][ny][1] = dist[x][y][0] + 1
                    q.append((nx, ny, 1))

    final = dist[N - 1][M - 1]
    if final[0] != 0 and final[1] != 0:
        return min(final[0], final[1])
    elif final[0] == 0 and final[1] == 0:
        return -1
    else:
        return final[0] or final[1]


if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    print(solution(N, M, matrix))
