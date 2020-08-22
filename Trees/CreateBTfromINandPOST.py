"""
Given inorder and postorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def breakInorder(self, array, val):
        i = 0
        while array[i] != val:
            i+=1
        return array[0:i], array[i+1:]

    def breakPostorder(self, array, s1, s2):
        return array[0:s1], array[s1:s1+s2]            
            

    def treehelper(self, Inorder, Postorder, node, direction):
        val = Postorder[-1]
        tempnode = TreeNode(val)
        if direction == "left": node.left = tempnode
        elif direction == "right": node.right = tempnode

        In1, In2 = self.breakInorder(Inorder, val)
        Po1, Po2 = self.breakPostorder(Postorder, len(In1), len(In2))
        if In1:
            self.treehelper(In1, Po1, tempnode, "left")
        if In2:
            self.treehelper(In2, Po2, tempnode, "right")

    def buildtree(self, Inorder, Postorder):
        val = Postorder[-1]
        headnode = TreeNode(val)
        In1, In2 = self.breakInorder(Inorder, val)
        Po1, Po2 = self.breakPostorder(Postorder, len(In1), len(In2))
        if In1:
            self.treehelper(In1, Po1, headnode, "left")
        if In2:
            self.treehelper(In2, Po2, headnode, "right")
        return headnode

def treeprint(node):
    if node is None:
        return
    nl, nr = None, None
    if node.right: nr = node.right.val
    if node.left: nl = node.left.val
    print("Node {} Left {} Right {}".format(node.val, nl, nr))
    treeprint(node.left)
    treeprint(node.right)

t = Solution()
A = [4, 2, 7,5,1,3,6]
B = [4,7,5,2,6,3,1]

node = t.buildtree(A, B)
treeprint(node)
