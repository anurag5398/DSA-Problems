"""
You are given A eggs, and you have access to a building with B floors from 1 to B.
Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor C with 0 <= C <= B such that any egg dropped at a floor higher than C will break, and any egg dropped at or below floor C will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= B).
Your goal is to know with certainty what the value of C is.
What is the minimum number of moves that you need to know with certainty what C is, regardless of the initial value of C
"""

class Solution:
    #@param A : int -> eggs
    #@param B : int -> floors
    #@return int
    def solve(self, A, B):
        dp = [[0 for _ in range(B + 1)] for _ in range(A + 1)]
        for f in range(1, B + 1):
            dp[1][f] = f
        for e in range(1, A + 1):
            dp[e][1] = 1

        for eggs in range(2, A + 1):
            for floor in range(2, B + 1):
                dp[eggs][floor] = float('inf')
                for bfloor in range(1, floor + 1):
                    temp = 1 + max(dp[eggs - 1][bfloor - 1], dp[eggs][floor - bfloor])
                    if temp < dp[eggs][floor]: dp[eggs][floor] = temp
        print(dp)
        return dp[A][B]

t = Solution()
print(t.solve(2, 10))