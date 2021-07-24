class Solution(object):
    def threeSum(self, nums: list[int])->list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 재귀 -> 시간초과
        # answer = []
        # nums.sort()
        # def go(nums: list[int], index: int, sum: int, cnt: int, nowlist: list[int]):
        #     if sum == 0 and cnt == 3 and nowlist not in answer:
        #         answer.append(nowlist)
        #         return
        #     if index >= len(nums) or cnt >= 3:
        #         return
        #     nowlist.append(nums[index])
        #     go(nums, index+1, sum+nums[index], cnt+1, nowlist[:])
        #     nowlist.pop()
        #     go(nums, index+1, sum, cnt, nowlist[:])
        #
        # go(nums, 0, 0, 0, [])
        #
        # return answer

        answer = []
        nums.sort()
        for i in range(len(nums)-2):
            # 중복 수 제거
            if i>0 and nums[i] == nums[i-1]:
                continue

            start, end = i+1, len(nums)-1
            while start<end:
                sum = nums[i] + nums[start] + nums[end]
                if sum < 0:
                    start+=1
                elif sum > 0:
                    end-=1
                else:
                    answer.append([nums[i], nums[start], nums[end]])

                    while start < end and nums[start] == nums[start+1]:
                        start+=1
                    while start < end and nums[end] == nums[end-1]:
                        end-=1
                    start+=1
                    end-=1
        return answer

a = Solution()
a.threeSum([-1,0,1,2,-1,-4])

