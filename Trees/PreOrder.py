"""
Given a binary tree, return the preorder traversal of its nodes values.
NOTE: Using recursion is not allowed.
"""
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
	    stack = []
	    root = A
	    ans = []
	    while len(stack) > 0 or root != None:
	        if root != None:
	            ans.append(root.val)
	            stack.append(root)
	            root = root.left
	        else:
	            node = stack.pop()
	            root = node.right
	    return ans