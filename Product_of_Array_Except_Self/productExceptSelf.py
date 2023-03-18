# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = [1]

        for i in range(1, len(nums)):
            result.append(result[-1]*nums[i-1])

        #Running sum product
        rsp=1

        for j in range(len(result)-2,-1,-1):
            rsp *= nums[j+1]
            result[j] *= rsp

        return result