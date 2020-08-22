"""
Rishik likes candies a lot. So, he went to a candy-shop to buy candies.
The shopkeeper showed him N packets each containg A[i] candies for cost of C[i] nibbles, each candy in that packet has a sweetness B[i]. The shopkeeper puts the condition that Rishik can buy as many complete candy-packets as he wants but he can't buy a part of the packet.
Rishik has D nibbles, can you tell him the maximum amount of sweetness he can get from candy-packets he will buy?
"""
#unbound knapsack
#sweetness = sweet/piece * pieces , cost
#dp[id][cost] = max sweetness

class Solution:
    #@param A : list of int -> number of candies
    #@param B : list of int -> sweetness
    #@param C : list of int -> cost
    #@param D : int -> max cost
    #@return int -> max sweetness
    def solve(self, A, B, C, D):
        for i, v in enumerate(A):
            A[i] = v * B[i]
        
        dp = [[0 for i in range(D + 1)] for i in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, D + 1):
                if j - C[i - 1] >= 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - C[i - 1]] + A[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[i][j]

A = [1, 2, 3]
B = [2, 2, 10]
C = [2, 3, 9]
D = 8
t = Solution()
print(t.solve(A, B, C, D))