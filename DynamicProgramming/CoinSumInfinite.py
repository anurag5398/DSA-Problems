"""
You are given a set of coins A. In how many ways can you make sum B assuming you have infinite amount of each coin in the set.
NOTE:
Coins in set A will be unique. Expected space complexity of this problem is O(B).
The answer can overflow. So, return the answer % (106 + 7).
"""
#to find ways(permutation), we can subtract from each coin

#to find unique ways(combination), we can subtract each value from all the coin i.e fix position of coin


class Solution:
    #@param A: list of int -> coins
    #@param B: int -> total
    #@return int -> ways
    def coinchange2(self, A, B):
        dp = [0 for i in range(B+1)]
        dp[0] = 1

        for coin in A:
            for i in range(coin, B+1):
                dp[i] = (dp[i] + dp[i-coin])%(10**6+7)
        
        return dp[B]%(10**6+7)

A = [1,2,3]
t = Solution()
print(t.coinchange2(A, 0))
                