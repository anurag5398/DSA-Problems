"""
Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)]. It is allowed to swap any two elements (not necessarily consecutive).

Find the minimum number of swaps required to sort the array in ascending order.


current-> 0(n^2) not accepted
req -> 0(nlogn)
"""

class Solution:
    def solve(self, A):
        swapcount = 0
        tempmax = max(A)
        for start in range(len(A)-1):
            smallvalue, smallindex = tempmax+1, -1
            for i in range(start, len(A)):
                if A[i] < smallvalue:
                    smallvalue, smallindex = A[i], i
            if smallindex != start:
                A[start], A[smallindex] = A[smallindex], A[start]
                swapcount+=1
        return swapcount




arr = [2, 0, 1, 3]

test = Solution()
print(test.solve( arr ))
