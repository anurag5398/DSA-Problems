"""
Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right, then right to left for the next level and alternate between).
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def zigzagLevelOrder(self, A):
        one, two = deque(), deque()
        flag = "LR"
        one.append(A)
        ans = []

        while len(one) > 0:
            temp = []
            while len(one) > 0:
                if flag == "LR":
                    x = one.popleft()
                    temp.append(x.val)
                    if x.left: two.append(x.left)
                    if x.right: two.append(x.right)
                elif flag == "RL":
                    x = one.pop()
                    temp.append(x.val)
                    if x.right: two.appendleft(x.right)
                    if x.left: two.appendleft(x.left)
            ans.append(temp)

            while len(two) > 0:
                x = two.popleft()
                one.append(x)
            
            flag = "RL" if flag=="LR" else "LR"
        return ans

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c
c.left = d
c.right = e

t = Solution()
print(t.zigzagLevelOrder(a))
