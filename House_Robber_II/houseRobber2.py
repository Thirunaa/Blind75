# Time Complexity : O(n) 
# Space Complexity : O(1)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1: return nums[0]

        profit1 = 0
        profit2 = 0
        for house in nums[1:]:
            profit1, profit2 = max(profit2+house, profit1), profit1

        profit3 = 0
        profit4 = 0
        for house in nums[:-1]:
            profit3, profit4 = max(profit4+house, profit3), profit3

        return max(profit1, profit3)