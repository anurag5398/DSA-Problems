"""
Given two sequences A and B, count number of unique ways in sequence A, to form a subsequence that is identical to the sequence B.
Subsequence : A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
"""
#dp[i][j] = number of ways to represent B[0..j] in A[0...i]
#base case 0 length pattern can be made by anything by deleting all i.e 1 way

class TLESolution:
    def ways(self, i, j, m, w):
        if j == len(m):
            self.ans+=1
            return
        if i == len(w):
            return
        if m[j] == w[i]:
            self.ways(i+1, j+1, m, w)
        self.ways(i+1, j, m, w)


    #@param A : string -> word
    #@param B : string -> match
    def numDistinct(self, A, B):
        self.ans = 0
        self.ways(0, 0, B, A)
        return self.ans


class Solution:
    #@param A : string -> word
    #@param B : string -> match
    def numDistinct(self, A, B):
        dp = [[0 for i in range(len(A) + 1)] for i in range(len(B) + 1)]
        for i in range(0, len(A) + 1):
            dp[0][i] = 1


        for i in range(1, len(B) + 1):
            for j in range(1, len(A) + 1):
                if B[i-1] == A[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[i][j]

t = Solution()
print(t.numDistinct("rabbbabbit", "rabbit"))