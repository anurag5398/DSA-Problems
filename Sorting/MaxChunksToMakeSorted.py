"""
Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)], if we split the array into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?
"""
#key array is from 0 to N-1

class Solution:
    def solve(self, A):
        chunks, maxval = 0, 0
        for index, value in enumerate(A):
            maxval = max(value, maxval)
            if maxval == index:
                chunks+=1
        return chunks

test = Solution()
print(test.solve([1,2,3,4,0]))