"""
Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.
You need to return the length of such longest common subsequence.
"""
class Solution:
    #@param A : string
    #@param B : string
    #@return an int : LCS
    def solve(self, A, B):
        sub = [[0 for i in range(len(B)+1)] for i in range(len(A)+1)]
        
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):

                if A[i-1] == B[j-1]:
                    sub[i][j] = sub[i-1][j-1] + 1
                
                else:
                    sub[i][j] = max(sub[i-1][j], sub[i][j-1])

        return sub[i][j]




t = Solution()
A = "aaaaaa"
B = "ababab"
print(t.solve(A, B))