"""
Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array.
Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
For Example: longest common prefix of "abcdefgh" and "abcefgh" is "abc".
"""
class Solution:
    def longestCommonPrefix(self, A):
        minlen = 999999
        for i in A:
            minlen = min(len(i), minlen)

        count = 0
        for i in range(minlen):
            temp = A[0][i]
            for all in A:
                if temp != all[i]:
                    return A[0][:count]
            count+=1
        return A[0][:minlen]

a = Solution()
A = ["abcd" , "abcdef", "abcdefgh"]
print(a.longestCommonPrefix(A))