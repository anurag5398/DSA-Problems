"""
Given a string A of size N.
Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
"""
class Solution:
    def solve(self, A):
        temp = A[-1::-1].split(" ")
        ans = ""
        for i, val in enumerate(temp):
            ans+= val[-1::-1]
            if i != len(temp)-1:
                ans+= " "
        print(ans)
        return ans

a = Solution()
a.solve("sky is blue")