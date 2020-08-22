"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""
from collections import OrderedDict
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def dictadd(self, key, val):
        if key in self.order:
            self.order[key].append(val)
        else:
            self.order[key] = [val]

    def bfs(self, node, lvl):
        if node == None:
            return
        self.dictadd(lvl, node.val)
        self.bfs(node.left, lvl+1)
        self.bfs(node.right, lvl+1)


    def levelOrder(self, A):
        self.order = OrderedDict()
        self.bfs(A, 0)
        return self.order.values()


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(17)

a.left = b
a.right = c
c.left = d
c.right = e

t = Solution()
print(t.levelOrder(a))