class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def travel(self, root):
        if root is None: return
        self.travel(root.right)
        self.travel(root.left)
        self.stack.append(root)

    def solve(self, A):
        self.stack = []
        self.travel(A)
        head = self.stack[-1]
        while self.stack:
            temp = self.stack.pop()
            temp.left = temp.right = None
            if self.stack: temp.right = self.stack[-1]
        return head
        


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(5)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

t = Solution()
h = t.solve(a)

while h:
    print(h.val, h.left, h.right)
    h = h.right