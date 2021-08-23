import collections
import heapq


class Solution(object):
    def networkDelayTime(self, times:list[list[int]], n:int, k:int)->int:
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # visit = [-1 for _ in range(n+1)]
        # graph = collections.defaultdict(list)
        # for u, v, w in times:
        #     graph[u].append([w, v])
        #
        # pq = [[0, k]]
        # visit[k] = 0
        #
        # while pq:
        #     front_w, front = heapq.heappop(pq)
        #     for weight, next in graph[front]:
        #         if visit[next] == -1 or visit[next] > (front_w + weight):
        #             visit[next] = visit[front] + weight
        #             heapq.heappush(pq, [visit[next], next])
        #
        # if -1 in visit[1:]:
        #     return -1
        # return max(visit)

        visit = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append([w, v])

        pq = [[0, k]]

        while pq:
            front_w, front = heapq.heappop(pq)
            if front not in visit:
                visit[front] = front_w
                for weight, next in graph[front]:
                    alt = visit[front] + weight
                    heapq.heappush(pq, [alt, next])

        if len(visit) == n:
            return max(visit.values())
        return -1

a = Solution()
a.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1)
a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)