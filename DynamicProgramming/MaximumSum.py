"""
You are given an array A of N integers and three integers B, C, and D.
You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.
"""
class Solution:
    #@param A : list of int
    #@param B, C, D : int
    #@return int
    def solve(self, A, B, C, D):
        ogiA = [i for i in A]
        for i, v in enumerate(A):
            A[i] = v * B
        prevMax = float('-inf')

        for i, v in enumerate(A):
            prevMax = max(prevMax, v)
            A[i] = prevMax + ogiA[i] * C

        prevMax, finalmax = float('-inf'), float('-inf')

        for i, v in enumerate(A):
            prevMax = max(prevMax, v)
            A[i] = prevMax + ogiA[i] * D
            finalmax = max(finalmax, A[i])

        return finalmax

t = Solution()
A = [3, 2, 1]
print(t.solve(A, 1, -10, 3))