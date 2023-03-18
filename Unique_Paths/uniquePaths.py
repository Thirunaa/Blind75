# Time Complexity : O(m*n) 
# Space Complexity : O(n)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prevrow = [1] *n

        if m ==1:
            return 1

        for i in range(m-1):
            currRow = [1]*n
            for j in range(n-2,-1,-1):
                currRow[j] = currRow[j+1] + prevrow[j]

            prevrow = currRow

        return currRow[0]