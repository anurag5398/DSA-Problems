"""
Given a binary tree of integers. Find the difference between the sum of nodes at odd level and sum of nodes at even level.
NOTE: Consider the level of root node as 1.
"""
class Solution:
    def solve(self, A):
        self.val = 0
        def oddEven(root, level):
            if root is None: return
            if level%2==0: self.val+= root.val
            else: self.val-= root.val
            oddEven(root.left, level+1)
            oddEven(root.right, level+1)
        oddEven(A, 0)
        return self.val