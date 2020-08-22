"""
Given preorder and inorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def breakIn(self, array, value):
        i = 0
        while i < len(array) and array[i] != value:
            i+=1
        return array[0:i], array[i+1:]

    def breakPr(self, array, size1, size2):
        return array[1:size1+1], array[size1+1:len(array)]

    def buildhelper(self, node, dir, pre, ino):
        #print("PRE ",pre," INORDER ",ino," len ",len(pre))
        newnode = TreeNode(pre[0])
        if dir == 'left': node.left = newnode
        elif dir == 'right': node.right = newnode

        In1, In2 = self.breakIn(ino, pre[0])
        Pr1, Pr2 = self.breakPr(pre, len(In1), len(In2))

        if Pr1: self.buildhelper(newnode, 'left', Pr1, In1)
        if Pr2: self.buildhelper(newnode, 'right', Pr2, In2)

    #A is preorder B is inorder
    def buildTree(self, A, B):
        Pre, In = A, B
        headnode = TreeNode(Pre[0])
        In1, In2 = self.breakIn(In, Pre[0])
        Pr1, Pr2 = self.breakPr(Pre, len(In1), len(In2))
        #print("PRE ",Pre," INORDER ",In)
        if len(Pr1) > 0: self.buildhelper(headnode, 'left', Pr1, In1)
        if len(Pr2) > 0: self.buildhelper(headnode, 'right', Pr2, In2)
        return headnode


A = [ 11, 14, 21, 20, 18, 28, 1, 10, 30, 26, 25, 8, 2, 4, 19, 27, 12, 6, 9, 23, 29, 17, 15, 31, 5, 16, 3, 24, 22, 13, 7 ]
B = [ 28, 1, 18, 10, 20, 30, 26, 25, 8, 2, 21, 4, 19, 14, 27, 11, 9, 23, 6, 17, 15, 29, 31, 12, 3, 16, 5, 24, 7, 13, 22 ]
t = Solution()
ans = t.buildTree(A, B)
def printtree(node):
    if node is None: return
    l, r = None, None
    if node.left: l = node.left.val
    if node.right: r = node.right.val
    print("Node {} Left {} Right {}".format(node.val, l, r))
    printtree(node.left)
    printtree(node.right)

printtree(ans)
