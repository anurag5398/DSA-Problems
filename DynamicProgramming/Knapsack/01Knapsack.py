"""
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
Also given an integer C which represents knapsack capacity.
Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.
NOTE:
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""
#dp[index][weight] = max value
A = [6, 10, 12]
B = [1, 2, 3]
C = 5

class Solution:
    #@param A : list of int -> value
    #@param B : list of int -> weight
    #@param C : int -> capacity
    #@return int -> max value
    def solve(self, A, B, C):
        dp = [[0 for i in range(C + 1)] for i in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(0, C + 1):
                dp[i][j] = dp[i-1][j]
                if j - B[i-1] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j - B[i-1]] + A[i-1])
                
        print(dp)
        return dp[i][j]

t = Solution()
print(t.solve(A, B, C))