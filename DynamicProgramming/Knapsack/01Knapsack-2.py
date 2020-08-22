"""
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
Also given an integer C which represents knapsack capacity.
Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.
NOTE: You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""
#in last 01 we took dp state weight by index for profit
#here complexity will reach 10^12 for same state
#we can take dp state index by profit for min weight
#dp[i][j] = dp[i-1][j] , dp[i-1][j- P[i]] + W[i] # i is index j is weight

class Solution:
    #@param A : list of int -> value
    #@param B : list of int -> weight
    #@param C : int -> capacity
    def solve(self, A, B, C):
        m = max(A) * len(A)
        dp = [[0 for i in range(m + 1)] for i in range(len(A) + 1)]
        for j in range(1, m + 1):
            dp[0][j] = 999999

        for i in range(1, len(A) + 1):
            for j in range(1, m + 1):
                if j - A[i-1] >= 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j - A[i-1]] + B[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        
        for j in range(m, -1, -1):
            if dp[len(A)][j] <= C and dp[len(A)][j] != 999999:
                return j


        

A = [1, 3, 2, 4]
B = [12, 13, 15, 19]
C = 10
t = Solution()
print(t.solve(A, B, C))