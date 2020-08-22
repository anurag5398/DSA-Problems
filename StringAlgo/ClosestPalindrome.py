"""
Groot has a profound love for palindrome which is why he keeps fooling around with strings.
A palindrome string is one that reads the same backward as well as forward.
Given a string A of size N consisting of lowercase alphabets, he wants to know if it is possible to make the given string a palindrome by changing exactly one of its character.
"""

class Solution:
    def solve(self, A):
        s = len(A)
        m, c = s//2, 0
        for i in range(m):
            if A[i] != A[s-i-1]:
                c+=1
        
        if   c == 0 and s%2==0: return "NO"
        elif c == 0 and s%2!=0: return "YES"
        elif c == 1: return "YES"
        else: return "NO"