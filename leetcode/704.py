class Solution:
    def search(self, nums: list[int], target: int) -> int:
        nums.sort()
        start, last = 0, len(nums)-1
        answer = -1
        while start<=last:
            mid = (start+last)//2
            if nums[mid]==target:
                answer = mid
                break
            elif nums[mid] > target:
                last = mid-1
            elif nums[mid] < target:
                start = mid+1
        return answer
a = Solution()
a.search([5], 0)
a.search([-1,0,3,5,9,12], 9)