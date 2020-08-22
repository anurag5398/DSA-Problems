"""
As it is Tushar's Birthday on March 1st, he decided to throw a party to all his friends at TGI Fridays in Pune. Given are the eating capacity of each friend, filling capacity of each dish and cost of each dish. A friend is satisfied if the sum of the filling capacity of dishes he ate is equal to his capacity. Find the minimum cost such that all of Tushar's friends are satisfied (reached their eating capacity).
NOTE:
Each dish is supposed to be eaten by only one person. Sharing is not allowed.
Each friend can take any dish unlimited number of times.
There always exists a dish with filling capacity 1 so that a solution always exists.
"""
#dp[id][capacity] = cost

class Solution:
    #@param A : list of int -> eating capacity
    #@param B : list of int -> filing capacity
    #@param C : list of int -> cost
    #@return int -> total cost
    def solve(self, A, B, C):
        mc = max(A)
        dp = [[0 for i in range(mc + 1)] for i in range(len(B) + 1)]

        for j in range(1, mc + 1):
            dp[0][j] = 99
        
        for i in range(1, len(B) + 1):
            for j in range(1, mc + 1):
                if j - B[i - 1] >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - B[i - 1]] + C[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        tc = 0
        for c in A:
            tc+= dp[i][c]
        return tc

A = [2, 4, 6]
B = [2, 1, 3]
C = [2, 5, 3]
t = Solution()
print(t.solve(A, B, C))