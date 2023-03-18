# Time Complexity : O(log n)
# Space Complexity : O(1)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) -1
        while low<=high:
            mid = low + (high-low)//2 #integer overflow
            if (nums[mid] == target):
                return mid
            if (nums[low] <= nums[mid]):   #left sorted
                if (nums[low]<=target and target < nums[mid]): #target is in range
                    high = mid-1 
                else:
                    low = mid+1
            else:  #right sorted
                if (nums[mid]<target and target<=nums[high]):
                    low=mid+1
                else:
                    high = mid-1   
        return -1