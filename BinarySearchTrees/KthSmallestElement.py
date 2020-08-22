"""
Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def kthsmallest(self, A, B):
        self.ans = -1
        self.B = B
        def travel(root):
            if root is None: return
            travel(root.left)
            self.B-=1
            if self.B == 0: self.ans = root.val
            travel(root.right)
        travel(A)
        return self.ans




a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(2)
e = TreeNode(8)


a.left = b
a.right = c
b.left = d
b.right = e

t = Solution()
t.kthsmallest(a, 4)