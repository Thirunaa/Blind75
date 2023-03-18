# Time Complexity : O(n*m) - n is the lenth of text 1 and m is the length of text 2 
# Space Complexity : O(n*m)
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1) #abcde
        n = len(text2) #ace
        grid = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if text1[i]==text2[j]:
                    grid[i][j] = 1+ grid[i+1][j+1]

                else:
                    grid[i][j] += max(grid[i][j+1],grid[i+1][j])


        return grid[0][0]
        
