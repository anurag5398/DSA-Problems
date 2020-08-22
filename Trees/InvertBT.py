"""
Given a binary tree A, invert the binary tree and return it.
Inverting refers to making left child as the right child and vice versa.
"""

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def invertTree(self, A):
	    def invert(root):
	        if root is None: return
	        invert(root.left)
	        invert(root.right)
	        root.left, root.right = root.right, root.left
	    invert(A)
	    return A
