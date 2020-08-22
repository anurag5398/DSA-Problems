"""
check if given binary tree is BST
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def isValidBST(self, A):
        self.bst = True
        #return (max, min)
        def checktree(root):
            if root is None: return (-99999, 99999)
            if self.bst is False: return
            l = checktree(root.left)
            r = checktree(root.right)
            if root.val < l[0] or root.val > r[1]:
                self.bst = False
            return max(root.val, r[0]), min(root.val, l[1])
        return 1 if self.bst else 0
