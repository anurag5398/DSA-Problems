"""
Given a binary tree A. Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly one edge on the original tree.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Weight:
    def __init__(self):
        self.val = 0

class Solution:
    def parse(self, root):
        def sumOfTree(root, w):
            if root is None: return
            l, r = Weight(), Weight()
            sumOfTree(root.left, l)
            sumOfTree(root.right, r)
            w.val = l.val + r.val + root.val
        w = Weight()
        sumOfTree(root, w)
        return w.val

    def solve(self, A):
        self.total = self.parse(A)
        self.ans = False
        def divide(root, w):
            if root is None: return
            if self.ans: return
            l, r = Weight(), Weight()
            divide(root.left, l)
            divide(root.right, r)
            w.val = l.val + r.val + root.val
            if w.val*2 == self.total:
                print(root.val)
                self.ans = True
        w = Weight()
        divide(A, w)
        return 1 if self.ans else 0


a = TreeNode(11)
b = TreeNode(-8)
c = TreeNode(3)
d = TreeNode(9)
e = TreeNode(-8)
f = TreeNode(4)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

t = Solution()
print(t.solve(a))