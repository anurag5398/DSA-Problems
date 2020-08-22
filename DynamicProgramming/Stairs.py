"""
You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    #n int
    #return int ways
    def ways(self, n):
        print(n)
        if self.dp[n] > 0: return self.dp[n]
        self.dp[n] = self.ways(n-1) + self.ways(n-2)
        return self.dp[n]


    #A int
    #return int total ways
    def climbStairs(self, A):
        self.dp = [0] * (A+1)
        self.dp[1], self.dp[2] = 1, 2
        return self.ways(A)


t = Solution()
print(t.climbStairs(10))