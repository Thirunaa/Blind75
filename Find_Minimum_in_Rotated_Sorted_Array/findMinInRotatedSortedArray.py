# Time Complexity : O(log n)
# Space Complexity : O(1)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1

        if nums[l]<= nums[h]:
            return nums[l]

        while l<=h:
            mid = (l+((h-l)//2))

            if nums[mid+1] < nums[mid]:
                return nums[mid+1]

            if nums[mid] >= nums[l]:
                l = mid+1
                

            else:
                h = mid-1