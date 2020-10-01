"""

problem link : https://www.acmicpc.net/problem/1932

"""


def solution(n: int):
    if n == 1:
        return triangle[0][0]

    memo = [[0] * i for i in range(1, n + 1)]
    memo[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                memo[i][j] = triangle[i][j] + memo[i - 1][j]
            elif j == i:
                memo[i][j] = triangle[i][j] + memo[i - 1][j - 1]
            else:
                memo[i][j] = max(memo[i - 1][j - 1], memo[i - 1][j]) + triangle[i][j]

    return max(memo[n - 1])


if __name__ == "__main__":
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n))
