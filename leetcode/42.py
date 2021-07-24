class Solution(object):
    def trap(self, height:list[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        left_max, right_max = height[0], height[-1]
        lp, rp = 0, len(height)-1
        answer = 0
        while lp<rp:
            left_max, right_max = max(left_max, height[lp]), max(right_max, height[rp])
            if left_max <= right_max:
                answer += left_max - height[lp]
                lp+=1
            else:
                answer += right_max - height[rp]
                rp-=1

        return answer

a = Solution()
a.trap([0,1,0,2,1,0,1,3,2,1,2,1])