"""
Given an integer array A denoting the Level Order Traversal of the Binary Tree.
You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.
NOTE:
In the array, the NULL/None child is denoted by -1.
"""
#Both Solution1 and Solution are working after increasing recursion stack limit.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

import sys
from collections import deque
sys.setrecursionlimit(10**6)
class Solution1:
    def solve(self, A):
        maxsize = len(A)
        headnode = TreeNode(A[0])
        Q = deque()
        last = 0
        Q.append((headnode, 0))
        while len(Q) > 0:
            node, index = Q.popleft()
            if index > maxsize: return headnode
            if node:
                index-=last
                left, right = 2*index+1, 2*index+2
                if A[left] != -1: child = TreeNode(A[left])
                else: child = None
                Q.append((child,left))
                node.left = child
                if A[right] != -1: child = TreeNode(A[right])
                else: child = None
                Q.append((child, right))
                node.right = child
            else:
                last+=1
        return headnode

class Solution2:
    def solve(self, A):
        maxsize = len(A)
        if len(A) < 3:
            print("Less than 3")
            return

        for i in range(maxsize):
            if A[i] != -1:
                A[i] = TreeNode(A[i])

        arr, Q = [], deque()
        Q.append(A[0])
        arr.append(A[1])
        arr.append(A[2])
        index, i = 3, 0

        while len(Q) > 0:
            while len(Q) > 0:
                x = Q.popleft()
                if i < len(arr) and arr[i] != -1:
                    x.left = arr[i]
                i+=1
                if i < len(arr) and arr[i] != -1:
                    x.right = arr[i]
                i+=1
            
            count = 0
            for i in arr:
                if i != -1: 
                    Q.append(i)
                    count+=1
            arr = []
            upper = index + 2*count
            if upper > maxsize: upper = maxsize
            for i in range(index, upper):
                arr.append(A[i])
            index = upper
            i = 0
        return A[0]

        

        

def printtree(node):
    if node is None: return
    l, r = None, None
    if node.left: l = node.left.val
    if node.right: r = node.right.val
    print("Node {} Left {} Right {}".format(node.val, l, r))
    printtree(node.left)
    printtree(node.right)

arr = [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]
t = Solution1()
ans = t.solve(arr)
printtree(ans)


arr2 = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]

ans2 = t.solve(arr2)
printtree(ans2) 