"""
Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.
The diameter of a tree is the number of edges on the longest path between two nodes in the tree.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Height:
    def __init__(self):
        self.H = 0

class Solution:
    def solve(self, A):
        self.max_diameter = 0
        def diameter(root, height):
            if root is None: return
            l, r = Height(), Height()
            diameter(root.left, l)
            diameter(root.right, r)

            height.H = max(l.H, r.H) + 1
            self.max_diameter = max(l.H+r.H, self.max_diameter)
        h = Height()
        diameter(A, h)
        return self.max_diameter



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

t = Solution()
print(t.solve(a))

