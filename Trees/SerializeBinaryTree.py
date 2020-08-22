"""
Given the root node of a Binary Tree denoted by A. You have to Serialize the given Binary Tree in the described format.
Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.
NOTE:
In the array, the NULL/None child is denoted by -1.
"""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def solve(self, A):
        pre, action = deque(), deque()
        pre.append(A)
        ans = []
        empty = TreeNode(-1)

        while len(pre) > 0:
            flag = False
            while len(pre) > 0:
                x = pre.popleft()
                if x.val != -1: flag = True
                ans.append(x.val)
                action.append(x)
            if flag:
                while len(action) > 0:
                    x = action.popleft()
                    if x.val != -1:
                        if x.left: pre.append(x.left)
                        else: pre.append(empty)

                        if x.right: pre.append(x.right)
                        else: pre.append(empty)
            else:
                return ans
        return ans

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