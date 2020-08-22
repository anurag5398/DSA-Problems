"""
Given a binary search tree.
Return the distance between two nodes with given two keys B and C. It may be assumed that both keys exist in BST.
NOTE: Distance between two nodes is number of edges between them.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    def findPath(self, root, val, path):
        if root is None: return []
        if root.val == val: 
            path.append(val)
            return path
        path.append(root.val)
        if val < root.val: 
            return self.findPath(root.left, val, path)
        else:
            return self.findPath(root.right, val, path)
        path.pop()
        

    def solve(self, A, B, C):
        path1 = self.findPath(A, B, [])
        path2 = self.findPath(A, C, [])
        i, j = 0, 0
        while i < len(path1) and j < len(path2):
            if path1[i] == path2[j]:
                i+=1
                j+=1
            else:
                break
        return len(path1)-i + len(path2)-j

a = Node(5)
b = Node(3)
c = Node(7)
d = Node(2)
e = Node(4)
a.left = b
a.right = c
b.left = d
b.right = e

t = Solution()
#x = t.findPath(a, 4, [])
#print(x)
print(t.solve(a, 5, 4))