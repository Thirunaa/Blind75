# Time Complexity : O(nlogn) 
# Space Complexity : O(1) - python does use extra space for sorting, but we can do sort in O(1) space
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)-1
        #sort the array
        nums.sort()

        result = []

        for i in range(n-1):
            if i>=1 and nums[i]==nums[i-1]:
                continue

            j = i+1
            k = n
            target = 0 - nums[i]

            while j<k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j] == nums[j+1]:
                        j+=1

                    while j<k and nums[k] == nums[k-1]:
                        k-=1

                    #go to the next new element
                    j+=1
                    k-=1

                else:
                    if target < (nums[j]+nums[k]):
                        k-=1
                    else:
                        j+=1

        return result