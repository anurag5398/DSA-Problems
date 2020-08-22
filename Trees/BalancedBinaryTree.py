"""
Given a root of binary tree A, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
#postorder traversal and while calculating height, check the balance for each node

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = self.left = None

class NodeHeight:
    def __init__(self):
        self.height = 0

class Solution:
    def calculate(self, root, height):
        if root is None: return
        if self.balanced is False: return

        lh, rh = NodeHeight(), NodeHeight()
        self.calculate(root.left, lh)
        self.calculate(root.right, rh)

        height.height = max(lh.height, rh.height) + 1
        if abs(lh.height - rh.height) > 1:
            self.balanced = False
            return


    def isBalanced(self, A):
        self.balanced = True
        height = NodeHeight()
        self.calculate(A, height)
        return 1 if self.balanced else 0



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

t = Solution()
print(t.isBalanced(a))
