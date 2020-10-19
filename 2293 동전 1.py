"""

problem link : https://www.acmicpc.net/problem/2293

"""


def solution():
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(n):
        for j in range(1, k + 1):
            if j - coins[i] >= 0:
                dp[j] += dp[j - coins[i]]

    return dp[k]


if __name__ == "__main__":

    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))

    print(solution())
