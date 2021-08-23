import itertools


class Solution(object):
    def subsets(self, nums:list[int])->list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        def dfs(index, path):
            if index>=len(nums):
                return
            answer.append(path)
            for i in range(index+1, len(nums)):
                dfs(i, path+[nums[i]])
        dfs(-1, [])
        return answer
        # answer = [[]]
        # if not nums:
        #     return answer
        # nums.sort()
        # for i in range(1, len(nums)+1):
        #     for comb in itertools.combinations(nums, i):
        #         answer.append(list(comb))
        # return answer

a = Solution()
a.subsets([1, 2, 3])