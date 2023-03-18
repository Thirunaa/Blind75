# Time Complexity : O(n*m) 
# Space Complexity : O(n*m)
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #rows : len(coins) +1
        #coumns : target amount
        dp = [[0 for _ in range(amount+1)] for s in range(len(coins)+1)]
        
        for j in range(1,amount+1):
            dp[0][j] = amount+1  # amount+1 is infinity here
            
        for i in range(1,len(coins)+1):
            for j in range(amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    dp[i][j] = min(dp[i-1][j], 1+ dp[i][j-coins[i-1]])
                    
        
        #print(dp)
        if dp[-1][-1] == amount+1: #infinity
            return -1
        
        return dp[-1][-1]