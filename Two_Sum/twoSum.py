# Time Complexity : O(n)
# Space Complexity : O(n) - Hashmap
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm ={}
        for i in range(len(nums)):
            # for every element check for the complement in the hashmap,
            c = target - nums[i]
            # if it is present return the index of the current element and the complement element's index
            if c in hm: # O(1) look up in hashmap
                return [hm[c],i]
            # first time when we look into the element store the element as the key and its index as the value
            hm[nums[i]] = i