"""
Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters in the beginning of the string.
Find and return how many minimum characters are needed to be inserted to make the string a palindrome string.
"""

class Solution:
    def ispalindrome(self, string):
        l = len(string)
        for i in range(l//2):
            if string[i] != string[l-i-1]: return False
        return True

    def solve(self, A):
        count = 0
        while True:
            if self.ispalindrome(A) is False: 
                A = A[0:-1]
                count+=1
            else: break
        return count
    


t = Solution()
print(t.solve("bb"))
