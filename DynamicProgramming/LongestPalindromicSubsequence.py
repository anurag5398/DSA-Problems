"""
Given a string A. Find the longest palindromic subsequence (A subsequence which does not need to be contiguous and is a palindrome).
You need to return the length of longest palindromic subsequence.
"""
class Solution:
    #@param A : string
    #@return int -> size of LPS
    def solve(self, A):
        lps = [[0 for i in range(len(A))] for i in range(len(A))]
        maxsize = 0

        for s in range(len(A)):
            for i in range(len(A)-s):
                j = i + s
                
                if i == j:
                    lps[i][j] = 1
                elif A[i] == A[j] and s == 1:
                    lps[i][j] = 2
                elif A[i] == A[j] and lps[i+1][j-1] > 0:
                    lps[i][j] = lps[i+1][j-1] + 2
                else:
                    lps[i][j] = max(lps[i][j-1], lps[i+1][j])
                maxsize = max(lps[i][j], maxsize)
        
        return lps[0][s]


t = Solution()
A = "aedsead"
print(t.solve(A))                  