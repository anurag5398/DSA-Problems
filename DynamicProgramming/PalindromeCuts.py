"""
Given a string A, partition A such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of A.
"""

class Solution:
    #@param A : string
    #@return int -> min cuts
    def minCut(self, A):
        dp = [[0 for i in range(len(A))] for i in range(len(A))]
        for k in range(len(A)):
            for i in range(len(A)-k):
                j = i + k
                if k == 0: dp[i][j] = 1
                elif k == 1:
                    if A[i] == A[j]:
                        dp[i][j] = 1
                else:
                    if A[i] == A[j]:
                        dp[i][j] = dp[i+1][j-1]

        cuts = [float('inf') for i in range(len(A))]
        for i in range(len(A)):
            if dp[0][i] == 1:
                cuts[i] = 0
                continue
            for j in range(i):
                if dp[j+1][i] == 1:
                    cuts[i] = min(cuts[i], 1 + cuts[j])

        return cuts[i]



t = Solution()
A = "abaaaca"
print(t.minCut(A))