# Time Complexity : O(n*m*(3^l)) - where l is the length of the word, 3 because we have 3 directions everytime, 4th directions is ignored becuase that is the path we come from
# Space Complexity : O(l) - recursive stack for DFS grows till length of the word
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        self.m = len(board)
        self.n = len(board[0])
        self.word =word
        self.board = board

        #edge case
        if len(word) > self.m*self.n:
            return False


        self.dirs = [[0,1],[-1,0],[1,0],[0,-1]]

        for i in range(self.m):
            for j in range(self.n):
                if self.word[0]==self.board[i][j]:
                    if self.dfs(i,j,0):
                        return True
        
        return False

    def dfs(self,i,j,index): # return type boolean

        #base
        if index == len(self.word):
            return True

        if i<0 or i==self.m or j<0 or j==self.n or self.board[i][j]=="#":
            return False

        
        if self.board[i][j]==self.word[index]:
            #action 
            self.board[i][j]="#"
            for x,y in self.dirs:
                nr = x+i
                nc = y+j
                #recurse
                if self.dfs(nr,nc,index+1):
                    return True

            #backtrack
            self.board[i][j] = self.word[index]

        return False
