class Solution(object):
    def twoSum(self, nums:list[int], target:int)->list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1 이중 포문
        #
        # first, second = 0, 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i] + nums[j])==target:
        #             first, second = i, j
        #             break
        # return [first, second]

        # 2 포문 한개, 탐색 2번
        #
        # first, second = 0, 0
        # for i in range(len(nums)):
        #     ano = target - nums[i]
        #     if ano in nums:
        #         if nums.index(ano) != i:
        #             first, second = nums[i], ano
        #             break
        #
        # return [first, second]

        # 3 포문 한개 탐색 1번, 딕셔너리로 한번에 탐색.
        num_map = map()
        for i, n in enumerate(nums):
            num_map[n] = i

        for i, n, in enumerate(nums):
            if target-n in num_map and i!=num_map[target-n]:
                return [i, num_map[target-n]]
a = Solution()
a.twoSum([2, 7, 11, 15], 9)

nums = [1, 2, 2, 2, 2, 1, 2, 2, 2]
print(nums[1:])
