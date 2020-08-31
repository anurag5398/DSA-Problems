"""
Given a binary tree T, find the maximum path sum.

The path may start and end at any node in the tree.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    #@param root : pointer to TreeNode
    #@return int -> max path till root
    def travel(self, root):
        if root is None: return 0
        l = self.travel(root.left)
        r = self.travel(root.right)
        pathSum = max(max(l, r) + root.val, root.val)
        self.totalSum = max(l + r + root.val, totalSum)
        return pathSum
    #@param A : pointer -> root of tree
    #@return int -> max path sum
    def maxPathSum(self, A):
        self.totalSum = float('-inf')
        self.travel(A)
        return self.totalSum
