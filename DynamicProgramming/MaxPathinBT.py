"""
Given a binary tree T, find the maximum path sum.
The path may start and end at any node in the tree.
"""
#for each node check if ans is this node i.e leftpath + curr, rightpath + curr, left+right+curr or just current

class Solution:
    def travel(self, root):
        if root is None: return 0
        l = self.travel(root.left)
        r = self.travel(root.right)
        self.maxpath = max(root.val, l + root.val, r + root.val, l + r + root.val, self.maxpath)
        return max(l + root.val, r + root.val, root.val)

    def maxPathSum(self, A):
        self.maxpath = 0
        self.travel(A)
        return self.maxpath