"""
Given a Binary Tree A with N nodes.
Write a function that returns the size of the largest subtree which is also a Binary Search Tree (BST).
If the complete Binary Tree is BST, then return the size of whole tree.
NOTE:
Largest subtree means subtree with most number of nodes.
"""
#52 mins
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None



def travel(root):
    global maxnodes
    if root is None: return (float('-inf'), float('inf'), 0, True)
    l = travel(root.left)
    r = travel(root.right)
    maxval = max(root.val, r[0])
    minval = min(root.val, l[1])
    isbst = True
    size = l[2]+r[2]+1
    if root.val < l[0] or root.val > r[1]:
        isbst = False
    isbst = isbst&l[3]&r[3]
    if isbst:
        maxnodes = max(size, maxnodes)
    return maxval, minval, l[2]+r[2]+1, isbst


a = TreeNode(5)
b = TreeNode(3)
c = TreeNode(8)
d = TreeNode(1)
e = TreeNode(4)
f = TreeNode(7)
g = TreeNode(9)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = g
c.left = f

maxnodes = 0
travel(a)
print(maxnodes)
