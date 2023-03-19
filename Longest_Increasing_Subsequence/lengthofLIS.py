# Time Complexity : O(n*n) 
# Space Complexity : O(n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i]) 
    
        return max(dp)
    
# Time Complexity : O(nlogn) 
# Space Complexity : O(n)  
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [nums[0]]

        for i in range(1, n):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                replace_index = self.binary_search(dp, nums[i])
                dp[replace_index] = nums[i]
        
        return len(dp)


    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + (r - l) // 2)
            
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
                
        return l