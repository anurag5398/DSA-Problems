"""
Given a binary tree. Check whether the given tree is a Sum-binary Tree or not.
Sum-binary Tree is a Binary Tree where the value of a every node is equal to sum of the nodes present in its left subtree and right subtree.
An empty tree is Sum-binary Tree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.
Return 1 if it sum-binary tree else return 0.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Weight:
    def __init__(self):
        self.val = 0


class Solution:
    def solve(self, A):
        if A is None: return 1
        self.sumBT = True
        def checktree(root, w):
            if root is None: return
            l, r = Weight(), Weight()
            checktree(root.left, l)
            checktree(root.right, r)
            if root.left or root.right:
                if root.val != l.val + r.val:
                    self.sumBT = False
            w.val = l.val + r.val + root.val
        w = Weight()
        checktree(A, w)
        return 1 if self.sumBT else 0




a = TreeNode(26)
b = TreeNode(10)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(6)
f = TreeNode(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

t = Solution()
print(t.solve(a))

            