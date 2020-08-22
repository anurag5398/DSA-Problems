"""
Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.
Right view of a Binary Tree is a set of nodes visible when the tree is visited from top.
Return the nodes in any order.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
from collections import deque

class Solution:
    def solve(self, A):
        nodes = dict()
        q = deque()
        q.append((A, 0))
        while q:
            node, vertical = q.popleft()
            nodes.setdefault(vertical, node.val)
            if node.left: q.append((node.left, vertical-1))
            if node.right: q.append((node.right, vertical+1))
        return list(nodes.values())
        



a = TreeNode(1)

t = Solution()
t.solve(a)
