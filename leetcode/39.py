import itertools


class Solution(object):
    def combinationSum(self, candidates:list[int], target:int)->list[list[int]]:
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer=[]
        candidates.sort()
        def dfs(index, sum, path):
            if sum > target:
                return
            elif sum==target:
                answer.append(path[:])
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i, sum+candidates[i], path)
                path.pop()
        dfs(0, 0, [])
        return answer

        # answer = []
        # candidates.sort()
        # last = target//candidates[0] + 1
        # for cnt in range(1, last):
        #     for comb in itertools.combinations_with_replacement(candidates, cnt):
        #         temp = sum(comb)
        #         if temp == target:
        #             answer.append(list(comb))
        #         # elif temp > target:
        #         #     break
        # return answer

a = Solution()
a.combinationSum([2, 3, 6, 7], 7)
a.combinationSum([2, 3, 5], 8)



k = (1, 2, 4)
print(type(k))
print(list(k))