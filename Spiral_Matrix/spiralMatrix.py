# Time Complexity : O(n*m) 
# Space Complexity : O(1) - we just use the result array which is not considered as an auxilary space
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n-1
        top = 0
        bottom = m-1

        result=[0] * (m*n)
        index=0

        while (index<(m*n)):
            #left to right
            for i in range(left,right+1):
                result[index] = matrix[top][i]
                index+=1
            top +=1

            #top to bottom
            for j in range(top,bottom+1):
                result[index] = matrix[j][right]
                index+=1
            right-=1

            if index==(m*n):
                break

            #right to left
            for k in range(right,left-1,-1):
                result[index] = matrix[bottom][k]
                index+=1
            bottom-=1

            #bottom to top
            for l in range(bottom,top-1,-1):
                result[index] = matrix[l][left]
                index+=1
            left+=1

        return result