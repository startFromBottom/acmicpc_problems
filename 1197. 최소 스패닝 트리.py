"""

problem link : https://www.acmicpc.net/problem/1197

"""


def solution() -> int:
    def find(n: int) -> int:
        if parents[n] != n:
            parents[n] = find(parents[n])
        return parents[n]

    def union(n1: int, n2: int) -> None:
        n1, n2 = find(n1), find(n2)
        if n1 != n2:
            if set_counts[n1] >= set_counts[n2]:
                parents[n2] = parents[n1]
                set_counts[n1] += set_counts[n2]
            else:
                parents[n1] = parents[n2]
                set_counts[n2] += set_counts[n1]

    min_cost = 0
    for u, v, w in costs:
        if find(u) == find(v):  # 같은 parents -> 동일 집합
            if set_counts[parents[u]] == V:
                break
            continue
        union(u, v)
        min_cost += w

    return min_cost


if __name__ == "__main__":

    costs = []
    parents = {}

    V, E = map(int, input().split())
    for _ in range(E):
        u, v, w = map(int, input().split())
        costs.append([u, v, w])
        parents[u] = u
        parents[v] = v
    costs.sort(key=lambda x: x[2])  # cost 기준 오름차순
    set_counts = {k: 1 for k in parents}

    print(solution())
