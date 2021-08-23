class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot = 0
        answer = 0
        left, right = 0, len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid-1

a=Solution()
a.search([4,5,6,7,0,1,2], 0)