# Time Complexity : O(n) 
# Space Complexity : O(1)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1
        two = 1

        if n==1:
            return 1

        for i in range(2,n+1):
            #temp = one
            #two = one + two
            #one = temp
            one, two = two, one+two

        return two
