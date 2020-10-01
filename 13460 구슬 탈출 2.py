"""

problem link : https://www.acmicpc.net/problem/13460

"""

from typing import List
from collections import deque


def solution(matrix: List[List[int]], r: (int, int), b: (int, int)):
    def move(x: int, y: int, dx: int, dy: int) -> (int, int, int):
        cnt = 0  # 이동 횟수, 빨간 공, 파란 공 이동 횟수에 따라 위치 조정
        while matrix[x + dx][y + dy] != "#" and matrix[x][y] != "O":
            x, y, cnt = x + dx, y + dy, cnt + 1
        return x, y, cnt

    visited = {(r[0], r[1], b[0], b[1])}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # 빨간공 x좌표, 빨간공 y 좌표, 파란공 x좌표, 파란공 y좌표, 이동 횟수
    q = deque([(r[0], r[1], b[0], b[1], 1)])

    while q:
        rx, ry, bx, by, num_move = q.popleft()
        if num_move > 10:
            return -1
        for dx, dy in directions:
            rnx, rny, rcnt = move(rx, ry, dx, dy)
            bnx, bny, bcnt = move(bx, by, dx, dy)
            if matrix[bnx][bny] != "O":
                if matrix[rnx][rny] == "O":
                    return num_move
                # 빨간 공, 파란 공 위치 겹칠 때 -> 빨간 공 or 파란 공 위치 조정해야!
                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx -= dx
                        rny -= dy
                    else:
                        bnx -= dx
                        bny -= dy
                if (rnx, rny, bnx, bny) not in visited:
                    visited.add((rnx, rny, bnx, bny))
                    q.append((rnx, rny, bnx, bny, num_move + 1))
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    r, b = (0, 0), (0, 0)

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == "R":
                r = (i, j)
            elif matrix[i][j] == "B":
                b = (i, j)

    print(solution(matrix, r, b))
