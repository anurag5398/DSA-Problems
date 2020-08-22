"""
Given a knapsack weight A and a set of items with certain value B[i] and weight C[i], we need to calculate maximum amount that could make up this quantity exactly.
This is different from classical Knapsack problem, here we are allowed to use unlimited number of instances of an item.
"""
#maintain 1D array, for each position check for each weights
#dp[i] = p[j] + dp[i - w[j]]

class Solution:
    #@param A : int -> capacity
    #@param B : list of int -> values
    #@param C : list of int -> weights
    #@return int -> maxValue
    def solve(self, A, B, C):
        dp = [0] * (A + 1)
        for i in range(min(C), A + 1):
            for j in range(len(C)):
                if i - C[j] >= 0:
                    dp[i] = max(dp[i - C[j]] + B[j], dp[i])
        return dp[A]

A = 80
B = [ 14, 13, 7, 5, 5, 7, 13, 16, 17, 1 ]
C = [ 10, 20, 9, 4, 15, 4, 4, 1, 15, 2 ]
t = Solution()
print(t.solve(A, B, C))