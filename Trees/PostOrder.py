"""
Given a binary tree, return the Postorder traversal of its nodes values.
NOTE: Using recursion is not allowed.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

from collections import deque

class Solution:
    #postorder traversal
    def postOrderTraversal(self, A):
        ans, stack = list(), list()
        root = A
        while len(stack) > 0 or root != None:
            if root:
                ans.append(root.val)
                stack.append(root)
                root = root.right
            else:
                x = stack.pop()
                root = x.left
        return ans[-1::-1]



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

t = Solution()
print(t.postOrderTraversal(a))