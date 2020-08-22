"""
In Danceland, one person can party either alone or can pair up with another person.
Can you find in how many ways they can party if there are A people in Danceland?
Note: Return your answer modulo 10003, as the answer can be large.
"""
#recursive
class Solution:
    # @param n : int
    # @return : int
    def ways(self, n):
        if self.dp[n] > 0: return self.dp[n]
        self.dp[n] = (self.ways(n-1) + self.ways(n-2)*(n-1))%10003
        return self.dp[n]

    # @param A : int
    # @return int
    def solve(self, A):
        self.dp = [0]*(A+1)
        self.dp[1], self.dp[2] = 1, 2
        return self.ways(A)%10003


#iterative
class Solution2:
    #@param A : int
    #return int
    def solve(self, A):
        if A < 3: return A
        dp = [0]*(A+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, A+1):
            dp[i] = (dp[i-1] + dp[i-2]*(i-1))%10003
        return dp[A]

t = Solution()
print(t.solve(25))

t2 = Solution2()
print(t.solve(25))