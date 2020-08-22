"""
Given an array A of size N, groot wants you to pick 2 indices i and j such that

1 <= i, j <= N
A[i] % A[j] is maximum among all possible pairs of (i, j).
Help Groot in finding the maximum value of A[i] % A[j] for some i, j.
"""

class Solution:
    def solve(self, A):
        if len(A) < 2:
            return -1
        
        i, j = 0, 0
        for value in A:
            if value > i and value > j:
                j = i
                i = value
            elif value < i and value > j:
                j = value
        return j%i

test = Solution()
print(test.solve([ 927, 707, 374, 394, 279, 799, 878, 937, 431, 112 ] ))
