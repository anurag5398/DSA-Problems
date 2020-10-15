"""
Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters in the beginning of the string.
Find and return how many minimum characters are needed to be inserted to make the string a palindrome string.
"""

class Solution:
    def calculate(self, A: str) -> list:
        n = len(A)
        lps = [None for _ in range(n)]
        length = 0
        lps[0] = 0

        i = 1
        while i < n:
            if A[i] == A[length]:
                length+=1
                lps[i] = length
                i+=1
            
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i+=1
        return lps

    def solve(self, A: str) -> int:
        revstring = A[::-1]

        concat = A + "$" + revstring

        lps = self.calculate(concat)

        return len(A) - lps[-1]

A = "abc"
t = Solution()
print(t.solve(A))