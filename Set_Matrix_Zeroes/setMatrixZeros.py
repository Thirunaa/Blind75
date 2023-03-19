# Time Complexity : O(n*m) 
# Space Complexity : O(max(m,n)) will be the size of the set
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # set to keep track of all the rows and columns that you have set zeros with
        iset = set()
        jset = set()
        m = len(matrix)
        n = len(matrix[0])
        # boolean to set the entire row to zeros if we come across one zero
        flag = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    iset.add(i)
                    jset.add(j)
                    flag=True
            # if the flag turns true it means we have encountered a zero, so set the entire row to be zeros       
            if flag:
                matrix[i] = [0]*n
                flag=False

        #iterate throught the matrix again to set the columns to zero, we can use iset to skip the rows that are already set to zeros
        for i in range(m):
            if i not in iset:
                for j in jset:
                     matrix[i][j]=0