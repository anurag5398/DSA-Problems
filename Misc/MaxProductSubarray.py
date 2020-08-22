"""
Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.
NOTE: Answer will fit in 32-bit integer value.
"""
class Solution:
    #@param A : list on int
    #@return int
    def maxProduct(self, A):
        current_max, current_min = A[0], A[0]
        overall_max = current_max

        for i, val in enumerate(A):
            if i == 0: continue
            last_max = current_max
            current_max = max(val, val*current_max, val*current_min)
            current_min = min(val, val*last_max, val*current_min)
            overall_max = max(current_max, overall_max)
        return overall_max