"""
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.
Each cell can have three values:
The value 0 representing an empty cell.
The value 1 representing a fresh orange.
The value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.
Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.
"""
#keep minheap with position of rotten with distance one.
#perform BFS and fill the cells one by one
from collections import deque
class Pos:
    def __init__(self, x, y):
        self.i, self.j = x, y
    def __lt__(self, other):
        return self.i <= other.j


class Solution:
    def isBounds(self, pos):
        if pos.i < 0 or pos.i >= self.n: return False
        if pos.j < 0 or pos.j >= self.m: return False
        return True

    def addNeighbors(self, matrix, pos, dis, Q):
        ic = [0, -1, 0, 1]
        jc = [-1, 0, 1, 0]
        for i, j in zip(ic, jc):
            newPos = Pos(pos.i + i, pos.j + j)
            if self.isBounds(newPos) and matrix[newPos.i][newPos.j] == 1:
                self.tempOneCount+=1
                Q.append((dis+1, newPos))
                self.maxdistance = max(dis+1, self.maxdistance)
                matrix[newPos.i][newPos.j] = 4
    #@param A : list of list of int
    #@return int -> max time/-1
    def solve(self, A):
        Q = deque()
        count1 = 0
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    count1+=1
                elif A[i][j] == 2:
                    Q.append((0, Pos(i, j)))
        
        self.tempOneCount, self.maxdistance = 0, 0
        self.n, self.m = n, m
        while Q:
            dis, pos = Q.popleft()
            self.addNeighbors(A, pos, dis, Q)

        if self.tempOneCount == count1:
            return self.maxdistance
        return -1

A = [   [1, 1, 1],
        [2, 1, 1],
        [1, 1, 1]   ]
t = Solution()
print(t.solve(A))

