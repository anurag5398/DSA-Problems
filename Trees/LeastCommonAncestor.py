"""
Find the lowest common ancestor in an unordered binary tree A given two values B and C in the tree.
Lowest common ancestor : the lowest common ancestor (LCA) of two nodes and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.
"""
#1 - give 1 weight to B and C and calculate sum in postorder, node with sum 2 is LCA. Handle case where parent and child are given in input or same 2 nodes are given
#2 - travel both path and see till which node path is same
#3 - find path in binary format, keep 1 and for each left add 0 for each right add 1


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class weight:
    def __init__(self):
        self.val = 0

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @param C : integer
	# @return an integer
	def present(self, root, val):
	    self.p = False
	    def parse(root, val):
	        if root is None: return
	        if root.val == val:
	            self.p = True
	        parse(root.left, val)
	        parse(root.right, val)
	    parse(root, val)
	    return self.p
	    
	    
	def lca(self, A, B, C):
	    if B == C:
	        if self.present(A, B): return B
	        else: return -1
	        
	    def find(root, w):
	        if root is None: return
	        l, r = weight(), weight()
	        find(root.left, l)
	        find(root.right, r)
	        if root.val == self.B or root.val == self.C:
	            temp = 1
	        else:
	            temp = 0
	        w.val = l.val + r.val + temp
	        if w.val == 2 and self.ans == -1:
	            self.ans = root.val
	    self.B, self.C = B, C
	    self.ans = -1
	    w = weight()
	    find(A, w)
	    return self.ans

            

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.left = b
a.right = c
b.left = d
b.right = e

t = Solution()
print(t.lca(a, 2, 5))
#print(t.ans)