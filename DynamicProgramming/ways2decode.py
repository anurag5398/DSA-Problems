"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7
"""

class Solution:
    #@param A : string
    #@return int
    def numDecodings(self, A):
        dp = [0]*(len(A)+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, len(A)+1):
            if int(A[i-1]) > 0:
                dp[i] = dp[i-1]
            if int(A[i-2]) == 1 or (int(A[i-2]) == 2 and int(A[i-1]) < 7):
                dp[i] = (dp[i] + dp[i-2])%(10**9+7)
        return dp[len(A)]%(10**9+7)

t = Solution()
print(t.numDecodings('308'))

