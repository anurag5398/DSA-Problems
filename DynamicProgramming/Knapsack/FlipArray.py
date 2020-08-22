"""
Given an array A of positive elements, you have to flip the sign of some of its elements such that the resultant sum of the elements of array should be minimum non-negative(as close to zero as possible).
Return the minimum number of elements whose sign needs to be flipped such that the resultant sum is minimum non-negative.
"""
#like a 0/1 knapsack where maccapacity can be 1/2 of total sum

class Solution:
    #@param A : list of int
    #@return int : total flips
    def solve(self, A):
        capacity = sum(A)//2
        dp = [[0 for _ in range(capacity + 1)] for _ in range(len(A) + 1)]
        for i in range(1, capacity + 1):
            dp[0][i] = 99

        minswaps = 99
        for i in range(1, len(A) + 1):
            for j in range(1, capacity + 1):
                dp[i][j] = dp[i-1][j]
                if j - A[i-1] >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j - A[i-1]] + 1)
        

        for j in range(capacity, -1, -1):
            for i in range(len(A), -1, -1):
                if dp[i][j] != 99:
                    minswaps = min(dp[i][j], minswaps)
            if minswaps != 99: return minswaps


A = [10, 22, 9, 33, 21, 50, 41, 60]
t = Solution()
print(t.solve(A))
