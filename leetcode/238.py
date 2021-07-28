class Solution(object):
    def productExceptSelf(self, nums: list[int])->list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 1, 1
        left, right = [], []
        for i in range(len(nums)):
            l*=nums[i]
            r *= nums[-i-1]
            left.append(l)
            right.insert(0, r)
        output = []
        for i in range(len(nums)):
            temp = 1
            if i>0:
                temp *= left[i-1]
            if i<len(nums)-1:
                temp *= right[i+1]
            output.append(temp)
        return output

a = Solution()
a.productExceptSelf([0,0])
a.productExceptSelf([1,2,3,4])