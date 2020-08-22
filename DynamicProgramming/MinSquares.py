"""
Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.
"""

class Solution:
    #@param A : int
    #return int
    def countMinSquares(self, A):
        if A < 2: return A
        dp = [0]*(A+1)
        dp[1] = 1
        for i in range(2, A+1):
            dp[i] = i
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i - j*j]+1)
        return dp[A]


t = Solution()
print(t.countMinSquares(6))

