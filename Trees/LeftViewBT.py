"""
Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.
Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side
NOTE: The value comes first in the array which have lower level.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
    
from collections import deque    
class Solution:
    def solve(self, A):
        Q = deque()
        Q.append((A, 0))
        ans = []
        while Q:
            node, lvl = Q.popleft()
            if lvl+1 > len(ans):
                ans.append(node.val)
            if node.left: Q.append((node.left, lvl+1))
            if node.right: Q.append((node.right, lvl+1))
        return ans
        