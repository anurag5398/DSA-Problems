"""
Given an integer array A of size N.
You can pick B elements from either left or right end of the array A to get maximum sum.
Find and return this maximum possible sum.
NOTE: Suppose B = 4 and array A contains 10 elements then:
You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.
"""
#we have to check all combinations, i.e left all right 0, left all-1 right 1, ....... left 0 right all
#for faster check of x elements from ay side, precompute prefix sum for finding sum in O(1)


class Solution:
    #@param A: list of int
    #@param B: int
    #@return int
    def solve(self, A: list, B: int) -> int:
        pre = [0 for i in range(len(A))]
        tempsum = 0
        for i, v in enumerate(A):
            tempsum+=v
            pre[i] = tempsum
        pre.insert(0, 0)
        last = len(A)
        maxpick = float('-inf')
        for left in range(B + 1):
            right = B - left
            tempval = pre[left] + ( pre[last] - pre[last - right] )
            maxpick = max(tempval, maxpick)
        return maxpick

t = Solution()
A = [5, -2, 3, 1, 2]
B = 3
print(t.solve(A, B))
        