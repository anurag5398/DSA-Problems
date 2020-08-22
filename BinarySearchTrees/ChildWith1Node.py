"""Given preorder traversal of a binary tree, check if it is possible that it is also a preorder traversal of a Binary Search Tree (BST), 
where each internal node (non-leaf nodes) have exactly one child.
"""

class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        maxval, minval = float('inf'), float('-inf')
        for i in range(len(A)-1):
            prev, curr = A[i], A[i+1]
            if curr < minval or curr > maxval:
                return "NO"
            if curr == prev: return "NO"
            elif curr > prev: minval = prev
            elif curr < prev: maxval = prev
        return "YES"