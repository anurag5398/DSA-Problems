"""
Given 2 strings A and B of size N and M respectively consisting of lowercase alphabets, find the lexicographically smallest string that can be formed by concatenating non empty prefixes of A and B (in that order).
Note: The answer string has to start with a non empty prefix of string A followed by a non empty prefix of string B.
"""
class Solution:
    def smallestPrefix(self, A, B):
        ans = ""
        ans+= A[0]
        for i in A[1:]:
            if i < B[0]:
                ans+= i
            else:
                break
        ans+= B[0]
        return ans



t = Solution()
print(t.smallestPrefix("abba","cdd"))
