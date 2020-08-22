"""
Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.
"""
#NotCompleted
import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class WrongSolution2:
    def adddict(self, key, val):
        if key in self.nodes:
            self.nodes[key].append(val)
        else:
            self.nodes[key] = [val]

    def verticalhelper(self, root, vertical, depth):
        if root is None: return
        self.adddict(vertical, (depth,root.val))
        self.verticalhelper(root.left, vertical-1, depth+1)
        self.verticalhelper(root.right, vertical+1, depth+1)

    def verticalOrderTraversal(self, A):
        self.nodes = dict()
        self.verticalhelper(A, 0, 0)
        for key in self.nodes.keys():
            self.nodes[key] = sorted(self.nodes[key])
        ans = []
        for key in sorted(self.nodes.keys()):
            temp = []
            for val in self.nodes[key]: temp.append(val[1   ])
            ans.append(temp)
        return ans

from collections import deque
class Solution:
    def adddict(self, key, val, tempdict):
        if key in tempdict:
            tempdict[key].append(val)
        else:
            tempdict[key] = [val]

    def verticalOrderTraversal(self, A):
        Q = deque()
        nodes = dict()
        Q.append((A, 0))
        minvertical, maxvertical = 0, 0
        while Q:
            node, vertical = Q.popleft()
            if node is None: return []
            self.adddict(vertical, node.val, nodes)
            minvertical = min(vertical, minvertical)
            maxvertical = max(vertical, maxvertical)
            if node.left: Q.append((node.left, vertical-1))
            if node.right: Q.append((node.right, vertical+1))
        ans = []
        for i in range(minvertical, maxvertical+1):
            ans.append(nodes[i])
        return ans


            

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
f.right = g

def printtree(head):
    if head is None: return
    print(head.val)
    if head.left:
        printtree(head.left)
    if head.right:
        printtree(head.right)

t = Solution()
print(t.verticalOrderTraversal(a))

