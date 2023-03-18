# Time Complexity : O(n) 
# Space Complexity : O(1)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        secondprev=nums[0]
        if len(nums)==1: return nums[0]
        prev=max(nums[0],nums[1])
        #logic
        for i in range(2,len(nums)):
            t = prev
            prev = max(nums[i]+secondprev, t)
            secondprev = t
        return prev