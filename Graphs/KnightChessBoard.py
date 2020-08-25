"""
Given any source point, (C, D) and destination point, (E, F) on a chess board of size A x B, we need to find whether Knight can move to the destination or not.
The above figure details the movements for a knight ( 8 possibilities ).
If yes, then what would be the minimum number of steps for the knight to move to the said point. If knight can not move from the source point to the destination point, then return -1.
NOTE: A knight cannot go out of the board.
"""
#Performed BFS
#All 3 solutions are working,
#last has the best space complexity since no recursion stack is used

import sys
import heapq
from collections import deque
sys.setrecursionlimit(10**6)

class SolutionWithArray:
    def isbound(self, i, j):
        if i < 0 or i >= self.A: return False
        if j < 0 or j >= self.B: return False
        return True


    #@param heap : heapq obj/list
    #@param arr : list of int
    def bfs(self, heap, arr):
        if not heap: return
        if self.ans != -1: return
        change_i = [-2, -1, 1, 2, 2, 1, -1, -2]
        change_j = [-1, -2, -2, -1, 1, 2, 2, 1]
        d, i, j = heapq.heappop(heap)
        if i == self.reqI and j == self.reqJ:
            self.ans = d
            return
        arr[i][j] = d
        for ci, cj in zip(change_i, change_j):
            if self.isbound(i + ci, j + cj) and arr[i + ci][j + cj] == -1:
                heapq.heappush(heap, (d + 1, i + ci, j + cj))
        self.bfs(heap, arr)
                
                

    #param A : int -> length of board
    #@param B : int -> breadth of board
    #@param C, D : int -> source coordinate
    #@param E, F : int -> destination coordinate
    def solve(self, A, B, C, D, E, F):
        arr = [[-1 for _ in range(B)] for _ in range(A)]
        arr[C - 1][D - 1] = 0
        self.A, self.B = A, B
        self.reqI, self.reqJ = E - 1, F - 1
        heap = []
        heapq.heappush(heap, (0, C - 1, D - 1))
        self.ans = -1
        self.bfs(heap, arr)
        return self.ans


class SolutionReecursive:
    #@param i, j : int
    #@return bool
    def isbound(self, i, j):
        if i < 0 or i >= self.A: return False
        if j < 0 or j >= self.B: return False
        return True


    #@param heap : heapq obj/list
    #@param arr : list of int
    def bfs(self, heap):
        if not heap: return
        if self.ans != -1: return
        change_i = [-2, -1, 1, 2, 2, 1, -1, -2]
        change_j = [-1, -2, -2, -1, 1, 2, 2, 1]
        d, i, j = heap.popleft()
        if i == self.reqI and j == self.reqJ:
            self.ans = d
            return
        self.visited.add((i, j))
        for ci, cj in zip(change_i, change_j):
            if self.isbound(i + ci, j + cj) and (i + ci, j + cj) not in self.visited:
                heap.append((d + 1, i + ci, j + cj))
        self.bfs(heap)
                
                

    #param A : int -> length of board
    #@param B : int -> breadth of board
    #@param C, D : int -> source coordinate
    #@param E, F : int -> destination coordinate
    def solve(self, A, B, C, D, E, F):
        self.visited = set()
        self.visited.add((C - 1, D - 1))
        self.A, self.B = A, B
        self.reqI, self.reqJ = E - 1, F - 1
        heap = deque()

        heap.append((0, C - 1, D - 1))
        self.ans = -1
        self.bfs(heap)
        return self.ans

class Solution:
    def isbound(self, i, j):
        if i < 0 or i >= self.A: return False
        if j < 0 or j >= self.B: return False
        return True

    def solve(self, A, B, C, D, E, F):
        self.A, self.B = A, B
        visited = set()
        q = deque()
        visited.add((C - 1, D - 1))
        q.append((0, C - 1, D - 1))

        while q:
            d, i, j = q.popleft()
            if i == E - 1 and j == F - 1: return d
            change_i = [-2, -1, 1, 2, 2, 1, -1, -2]
            change_j = [-1, -2, -2, -1, 1, 2, 2, 1]
            for ci, cj in zip(change_i, change_j):
                if self.isbound(i + ci, j + cj) and (i + ci, j + cj) not in visited:
                    q.append((d + 1, i + ci, j + cj))
                    visited.add((i + ci, j + cj))
        return -1
            

A = 14
B = 17
C = 10
D = 15
E = 2
F = 10
t = Solution()
print(t.solve(A, B, C, D, E, F))

