# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #globalMaximum = float("-inf")
        # becuase in the question it is mentioned that the minimum value could be -10
        globalMaximum = -10

        currentMinimum = 1
        currentMaximum = 1

        for num in nums:
            currentMinimum, currentMaximum = min(currentMinimum * num, currentMaximum * num, num), max(currentMinimum * num, currentMaximum * num, num)
            globalMaximum = max(globalMaximum, currentMaximum)


        return globalMaximum
    
    
# FOLLOW UP QUESTION - WHAT IF WE HAVE TO RETURN/PRINT THE MAXIMUM PRODUCT SUBARRAY
# UPVOTE FOR MY POST, IF YOU LIKE THE SOLUTION - https://leetcode.com/problems/maximum-product-subarray/solutions/3286073/follow-up-question-also-print-return-the-maximum-product-subarray/
# Time Complexity : O(n)
# Space Complexity : O(1)
'''
Intuition
Have an end pointer to the index whenever you update global maximum. After traversing the array fully, have a seperate while to see what is the potential starting point of the maximum product subarray.

Approach
Every time global maximum is updated, we reset the end of the subarray. So we move from back to find what could be possible starting of that subarray that contributes to maximum product.

While moving the starting pointer if we encounter some number to be 0, the start pointer stops there, or if the number itself has contributed for the globalMaximum at that point, IT MEANS NO VALUE BEFORE THAT POINT HAS CONTRIBUTED TO THE MAXIMUM PRODUCT. Moving back from end to potential start point using j pointer, at every point we divide contributed value by the number itself to move backwards in search of finding the starting point of subarray.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        currentMinimum = nums[0]
        currentMaximum = nums[0]
        globalMaximum = nums[0]

        start = 0
        end = 1

        for i in range(1,len(nums)):
            currentMinimum, currentMaximum  = min(currentMinimum * nums[i], currentMaximum * nums[i], nums[i]), max(currentMinimum * nums[i], currentMaximum * nums[i], nums[i])
            
            if (currentMaximum > globalMaximum):
                globalMaximum = currentMaximum
                end=i+1
                

        j=end-1
        while j>=0:
            if nums[j]==0:
                start = j
                break
            else:
                if globalMaximum == nums[j]:
                    start = j
                    break
                globalMaximum = globalMaximum/nums[j]
            j-=1

        #nums[start: end] is the maximum product subarray
        prod = 1
        for num in nums[start: end]:
            prod *=num

        return prod