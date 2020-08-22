"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
"""
#added path to check
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    #A root B sum
    def hasPathSum(self, root, B):
        if root is None:
            if B == 0: return 1
            else: return 0
        else:
            ans = 0
            tempsum = B - root.val
            if tempsum == 0 and root.left == None and root.right == None:
                return 1
            
            if root.left: 
                ans = ans or self.hasPathSum(root.left, tempsum)
            if root.right: 
                ans = ans or self.hasPathSum(root.right, tempsum)
            return ans


class Solution2:
    def hasPathSum(self, root, B):
        def checkPath(root, B):
            if root is None:
                if B == 0:
                    self.ans = True
                return
            else:
                B = B - root.val
                if B == 0 and root.left == None and root.right == None:
                    self.ans = True
                    return
                if root.left: checkPath(root.left, B)
                if root.right: checkPath(root.right, B)
        self.ans = False
        checkPath(root, B)
        return 1 if self.ans else 0

a = TreeNode(1000)
b = TreeNode(2000)
c = TreeNode(-3002)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
b.left = c
#b.left = d
#d.right = e

t = Solution()
print(t.hasPathSum(a, -1))

