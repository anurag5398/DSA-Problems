"""
You are given A eggs, and you have access to a building with B floors from 1 to B.
Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor C with 0 <= C <= B such that any egg dropped at a floor higher than C will break, and any egg dropped at or below floor C will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= B).
Your goal is to know with certainty what the value of C is.
What is the minimum number of moves that you need to know with certainty what C is, regardless of the initial value of C
"""
#consider for each floor we have 2 choice: egg breaks and does not break
#if breaks dp[egg - 1][floor - 1] (below part of that floor and one less egg)
#dosent break dp[egg][length of building - floor] (same number of eggs and the upper half of the building)

#Now start with building of height 2 (1 and 0 base case), and built the building for each number of eggs



class Solution:
    #@param A : int -> eggs
    #@param B : int -> floors
    #@return int
    def solve(self, A, B):
        dp = [[0 for _ in range(B + 1)] for _ in range(A)]
        for floor in range(B + 1):
            dp[0][floor] = floor
        for eggs in range(A):
            dp[eggs][1] = 1
            dp[eggs][0] = 0
        
        for egg in range(1, A):
            for floor in range(2, B + 1):
                dp[egg][floor] = float('inf')
                for dropfloor in range(1, floor):
                    dp[egg][floor] = min(1 + max(dp[egg-1][dropfloor-1], dp[egg][floor-dropfloor]), dp[eggs][floor])

        print(dp)
        return dp[A-1][B]
t = Solution()
print(t.solve(3, 14))