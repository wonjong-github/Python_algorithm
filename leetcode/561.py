class Solution(object):
    def arrayPairSum(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums.sort()
        a = sorted(nums)
        answer = sum(nums[::2])
        return answer


a = Solution()
a.arrayPairSum([6, 2, 6, 5, 1, 2])
