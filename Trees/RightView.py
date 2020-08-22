"""
Given a binary tree of integers denoted by root A. Return an array of integers representing the right view of the Binary tree.
Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = self.left = None

class NotWorkingSolution:
    def calculate(self, root, level, vertical):
        if root is None: return
        if level in self.leveldict:
            if self.leveldict[level][1] < vertical:
                self.leveldict[level] = (root.val, vertical)
        else:
            self.leveldict[level] = (root.val, vertical)
        
        self.calculate(root.left, level+1, vertical-1)
        self.calculate(root.right, level+1, vertical+1)

    def solve(self, A):
        self.leveldict = dict()
        self.calculate(A, 0, 0)
        ans = []
        for key in sorted(self.leveldict.keys()):
            ans.append(self.leveldict[key][0])
        return ans

class Solution:
    def solve(self, A):
        root = A
        stack = [(root, 0)]
        max_depth = -1
        level_dict = dict()
        while stack:
            val, depth = stack.pop()
            if val:
                max_depth = max(depth, max_depth)
                level_dict.setdefault(depth, val.val)
                stack.append((val.left, depth+1))
                stack.append((val.right, depth+1))
        return [level_dict[key] for key in range(max_depth+1)]

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

t = Solution()
print(t.solve(a))


