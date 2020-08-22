"""
Given a string B, find if it is possible to re-order the characters of the string B so that it can be represented as a concatenation of A similar strings.
Eg: B = aabb and A = 2, then it is possible to re-arrange the string as "abab" which is a concatenation of 2 similar strings "ab".
If it is possible, return 1, else return -1.
"""
class Solution:
    def adddict(self, value, tempdict):
        if value in tempdict:
            tempdict[value]+=1
        else:
            tempdict[value] = 1
    def solve(self, A, B):
        freq = dict()
        for i in range(len(B)):
            self.adddict(B[i], freq)

        for vals in freq.values():
            if vals%A != 0:
                return -1

        return 1

a = Solution()
A = "bc"
print(a.solve(1, A))