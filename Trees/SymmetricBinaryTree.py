"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""
class Solution:
	# @param A : root node of tree
	# @return an integer
	def checksame(self, root1, root2):
	    if self.same is False: return
	    if root1 is None and root2 is None: return
	    if root1 is None and root2 != None:
	        self.same = False
	        return
	    if root2 is None and root1 != None:
	        self.same = False
	        return
	    if root1.val != root2.val:
	        self.same = False
	        return
	    self.checksame(root1.left, root2.right)
	
	def isSymmetric(self, A):
	    self.same = True
	    self.checksame(A, A)
	    return 1 if self.same else 0    