# Time Complexity : O(n)
# Space Complexity : O(n) - Hashset
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for ele in nums:
            if ele in hashset:
                return True

            hashset.add(ele)

        return False