"""
Given a positive integer n, find the number of non-negative binary rep. of size n, whose binary representations do NOT contain consecutive ones.
"""
#if we add another digit, if the last digit was 1 only 0 could be added, else both 0 and 1 could be added
#the pattern follows fibbonaci like structure

class Solution:
    def findIntegers(self, num: int) -> int:
        zero, one = 1, 1
        for i in range(2, num):
            zero, one = zero + one, zero
        return zero + one

t = Solution()
print(t.findIntegers(5))
