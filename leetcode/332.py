import collections


class Solution(object):
    def findItinerary(self, tickets:list[list[str]])->list[str]:
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for t in sorted(tickets):
            graph[t[0]].append(t[1])
        answer = []
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop(0))
            answer.append(start)
        dfs("JFK")
        return answer[::-1]

        # tickets.sort()
        # used = [0 for _ in range(len(tickets))]
        # def dfs(start, path):
        #     if sum(used) == len(tickets):
        #         global answer
        #         answer = path
        #         return 1
        #     for i in range(len(tickets)):
        #         if tickets[i][0] == start and used[i] == 0:
        #             used[i] = 1
        #             if dfs(tickets[i][1], path+[tickets[i][1]]):
        #                 return 1
        #             used[i] = 0
        #     return 0
        # dfs("JFK", ["JFK"])
        # return answer

a = Solution()
a.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
a.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])