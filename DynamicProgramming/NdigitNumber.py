"""
Find out the number of A digit positive numbers, whose digits on being added equals to a given number B.
Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.
Since the answer can be large, output answer modulo 1000000007
"""
#dp[i][j] -> for size of i , how many numbers with sum j
#base for 1 digit count = 1 except 0
#by adding extra digit sum can change by 1-9

class Solution:
    #@param A : int -> len
    #@param B : int -> sum
    #@return int
    def solve(self, A, B):
        dp = [[0 for i in range(B+1)] for i in range(A)]
        top = min(10, B+1)
        for i in range(1, top):
            dp[0][i] = 1
        
        for i in range(1, A):
            for j in range(1, B+1):
                for k in range(0, 10):
                    if j-k >= 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-k])%(10**9+7)

        return dp[A-1][B]%(10**9+7)

t = Solution()
print(t.solve(75,22))