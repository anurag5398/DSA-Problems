"""
Given a binary tree, return the inorder traversal of its nodes values.
NOTE: Using recursion is not allowed.
"""

#recursion
def inorder(root):
    if root is None: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, val):
        self.stack.append(val)
        self.count+=1
    def pop(self):
        if self.count > -1:
            temp = self.stack.pop()
            self.count-=1
            return temp
        return None
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return None
    def isempty(self):
        if self.count > -1:
            return False
        else:
            return True

class Solution:
    def inorderTraversal(self, A):
        root = A
        stack = Stack()
        ans = []
        while stack.count > -1 or root != None:
            if root != None:
                stack.push(root)
                root = root.left
            else:
                x = stack.pop()
                ans.append(x.val)
                root = x.right
        return ans
