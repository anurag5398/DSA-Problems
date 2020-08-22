"""
Find the longest increasing subsequence of a given array of integers, A.
In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible.
In this case, return the length of the longest increasing subsequence.
"""
#maxlength is 2500

class Solution:
    #@param A : list of int 
    #@return int -> lis
    def lis(self, A):
        ls = [0] * len(A)
        ls[0] = 1
        maxls = 0
        for i in range(1, len(A)):
            for j in range(0, i):
                if A[j] < A[i] and ls[j] >= ls[i]:
                    ls[i] = ls[j]
            ls[i]+=1
            maxls = max(ls[i], maxls)
        return maxls


t = Solution()
A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(t.lis(A))