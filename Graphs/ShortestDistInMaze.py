"""
Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.
1 represents a wall in a matrix and 0 represents an empty location in a wall.
There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.
Find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the starting position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.
"""
#Solution1 is just for fun, has huge TC (due to lot of functions and adding to visited while popping and not while pushing)



from collections import defaultdict
from heapq import heappop, heappush
class Node:
    def __init__(self, x, y):
        self.i = x
        self.j = y
    def __lt__(self, obj):
        return self.i <= obj.i

class Solution:
    def isBound(self, node):
        if node.i < 0 or node.i >= self.n: return False
        if node.j < 0 or node.j >= self.m: return False
        if self.A[node.i][node.j] == 1: return False
        return True

    def nodeadd(self, n1, n2):
        return Node(n1.i + n2.i, n1.j + n2.j)

    def nodesub(self, n1, n2):
        return Node(n1.i - n2.i, n1.j - n2.j)

    def checkzero(self, node):
        if self.A[node.i][node.j] == 0: return True
        return False

    def isdiff(self, n1, n2):
        if n1.i == n2.i and n2.j == n1.j: return False
        return True

    def move(self, node, parent, d, heap):
        change = [Node(-1, 0), Node(0, -1), Node(1, 0), Node(0, 1)]
        for cn in change:
            td = 0
            tnode = node
            newnode = self.nodeadd(tnode, cn)
            while self.isBound(newnode) and self.isdiff(newnode, parent):
                tnode = newnode
                td+=1
                newnode = self.nodeadd(newnode, cn)
            if td != 0:
                if tnode not in self.visited:
                    heappush(heap, (d + td, tnode, self.nodesub(tnode, cn)))

    def solve(self, A, B, C):
        self.A = A
        self.n, self.m = len(A), len(A[0])
        totalcells = self.n * self.m
        goal = Node(C[0], C[1])
        self.visited = set()
        self.visited.add()
        h = [(0, Node(B[0], B[1]), Node(-1, -1))]
        while h:
            d, n, p = heappop(h)
            #self.visited.add(n)
            #print(d)
            if d > totalcells//2: return -1
            self.move(n, p, d, h)
        
        return -1


class Solution2:
    #@param i, j: int
    #@return bool
    def isavail(self, i, j):
        if i < 0 or i >= self.n: return False
        if j < 0 or j >= self.m: return False
        if self.A[i][j] == 1: return False
        return True

    #@param A : list of list of int
    #@param B, C : list of int
    #@return int  
    def solve(self, A, B, C):
        self.A = A
        self.n, self.m = len(A), len(A[0])
        change_i = [0, 0, -1, 1]
        change_j = [-1, 1, 0, 0]
        visited = set()
        visited.add((B[0], B[1]))
        h = [(0, B[0], B[1])]
        while h:

            d, i, j = heappop(h)
            if i == C[0] and j == C[1]: return d
            for ci, cj in zip(change_i, change_j):
                ti, tj, td = i, j, 0
                while self.isavail(ti + ci, tj + cj):
                    ti+=ci
                    tj+=cj
                    td+=1
                if td != 0 and (ti, tj) not in visited:
                    heappush(h, (d + td, ti, tj))
                    visited.add((ti, tj))
        return -1





A = [
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
B = [ 0, 0 ]
C = [ 3, 3 ]
t = Solution2()
print(t.solve(A, B, C))