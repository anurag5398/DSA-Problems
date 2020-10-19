"""
Two elements of a binary search tree (BST),represented by root A are swapped by mistake. Tell us the 2 values swapping which the tree will be restored.
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""

#Current solution is with o(n) space.
#inorder of bst is sorted

class Solution:
    #@param root: TreeNode
    def inorder(self, root: TreeNode):
        if root is None: return
        self.inorder(root.left)
        self.tra.append(root.val)
        self.inorder(root.right)
        
	# @param A : root node of tree
	# @return a list of integers
	def recoverTree(self, A: TreeNode) -> list:
	    a1, a2 = None, None
	    self.tra = list()
	    self.inorder(A)
	    n = len(self.tra)
	    for i in range(n - 1):
	        curr, next = self.tra[i], self.tra[i + 1]
	        if next < curr:
	            a1, a2 = curr, next
	            self.tra.pop(i)
	            break
	    for i in range(n - 2):
	        curr, next = self.tra[i], self.tra[i + 1]
	        if next < curr:
	            a2 = next
	            break
	    return [a2, a1]