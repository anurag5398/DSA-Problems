"2 nodes add up to a sum or not"

class Solution:
    def traverse(self, root):
        if root is None: return
        self.traverse(root.left)
        self.inorder.append(root.val)
        self.traverse(root.right)
    def t2Sum(self, A, B):
        self.inorder = []
        self.traverse(A)
        i, j = 0, len(self.inorder)-1
        while i < j:
            if self.inorder[i]+self.inorder[j] > B:
                j-=1
            elif self.inorder[i]+self.inorder[j] < B:
                i+=1
            elif self.inorder[i]+self.inorder[j] == B:
                return 1
        return 0