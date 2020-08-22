"""
Given a strictly increasing array A of positive integers forming a sequence.
A sequence X1, X2, X3, ..., XN is fibonacci like if
N > =3
Xi + Xi+1 = Xi+2 for all i+2 <= N
Find and return the length of the longest Fibonacci-like subsequence of A.
If one does not exist, return 0.
NOTE: A subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.
"""

class Solution:
    #@param A : list of int
    #@return int
    def solve(self, A):
        Aset = set(A)
        maxlen = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                c = 2
                f, s = A[i], A[j]
                while (f+s) in Aset:
                    c+=1
                    f, s = s, f+s
                maxlen = max(c, maxlen)
        return maxlen if maxlen != 2 else 0

t = Solution()
A = [1,2,3,4,4,5,6,7,8]
print(t.solve(A))