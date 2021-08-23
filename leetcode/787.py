import collections
import heapq
import sys


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # visit = [sys.maxsize for _ in range(n)]
        graph = collections.defaultdict(list)
        for u, w, p in flights:
            graph[u].append([w, p])

        pq = [[0, src, k]]
        # visit[src] = 0
        while pq:
            front_w, front, front_k = heapq.heappop(pq)
            if front == dst:
                return front_w
            if front_k >= 0:
                for v, w in graph[front]:
                    heapq.heappush(pq, [front_w + w, v, front_k-1])
        return -1

a = Solution()
# a.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
a.findCheapestPrice(5,
[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],
0,
2,
2)