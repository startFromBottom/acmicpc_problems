"""

problem link : https://www.acmicpc.net/problem/16947

"""
from collections import defaultdict, deque


def solution():
    # visited 값
    # visited[i] = 2 -> i : cycle에 포함된 노드
    # visited[i] = -2 -> i : 그래프에서 cycle은 있으나, cycle에 속하지 않은 노드
    # visited[i] = -1 -> i : 그래프 내에 cycle이 존재하지 않는 경우
    visited = [0] * 3000
    # dist(cycle로 부터의 거리 저장) 값
    # dist[i] = -1 -> i : cycle에 포함되지 않은 노드
    dist = [0] * 3000

    def dfs(cur, prev):
        """
        :param cur: current node number
        :param prev: prev node number
        :return:
        """
        # 이미 방문한 점을 찾았을 때 -> 사이클 찾음
        if visited[cur] == 1:
            return cur
        visited[cur] = 1
        for next in graph[cur]:
            if next == prev:  # 이전 정점으로 되돌아 가는 거 고려 x
                continue
            res = dfs(next, cur)
            if res == -2:
                return -2
            if res >= 0:  # cycle에 해당하는 node
                visited[cur] = 2
                return -2 if cur == res else res  # cycle 시작점부터 -2로 기록
        return -1

    def bfs():
        q = deque()
        for i in range(N):
            # cycle에 포함되는 경우
            if visited[i] == 2:
                q.append(i)
            else:  # cycle에 포함되지 않은 경우
                dist[i] = -1
        while q:
            cur = q.popleft()
            for next in graph[cur]:
                if dist[next] == -1:  # 방문하지 않은 정점
                    q.append(next)
                    dist[next] = dist[cur] + 1

    dfs(0, -1)
    bfs()
    return dist


if __name__ == "__main__":

    N = int(input())
    graph = defaultdict(list)

    for _ in range(N):
        w, v = map(int, input().split())
        graph[w-1].append(v-1)
        graph[v-1].append(w-1)

    print(" ".join([str(i) for i in solution()[:N]]))
