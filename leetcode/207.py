import collections


class Solution(object):
    def canFinish(self, numCourses:int, prerequisites:list[list[int]])->bool:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        trace = []
        visit = []
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(start):
            if start in trace:
                return False
            if start in visit:
                return True
            trace.append(start)
            for next in graph[start]:
                if not dfs(next):
                    return False
            trace.remove(start)
            visit.append(start)
            return True

        l = list(graph)
        for k in list(graph):
            if not dfs(k):
                return False

        return True

a = Solution()
# a.canFinish(2, [[1,0],[0,1]])
a.canFinish(3, [[0, 1], [0, 2], [1, 2]])

a.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])