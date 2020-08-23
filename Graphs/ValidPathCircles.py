"""
There is a rectangle with left bottom as (0, 0) and right up as (x, y).
There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.
Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.
"""
#for each cell check if any circle center has >= R distance\
# perform dfs 
import sys
import math
sys.setrecursionlimit(10**7)
class Pos:
    def __init__(self, x, y):
        self.i, self.j = x, y

class Solution:
    def notInBound(self, cell):
        if cell.i < 0 or cell.i >= self.n: return True
        if cell.j < 0 or cell.j >= self.m: return True
        return False

    def travel(self, cell, arr):
        if self.notInBound(cell): return False
        if arr[cell.i][cell.j] != 0: return False
        if cell.i == self.n - 1 and cell.j == self.m - 1:
            return True
        arr[cell.i][cell.j] = 2
        change_i = [-1, -1, 0, 1, 1, 1, 0, -1]
        change_j = [0, 1, 1, 1, 0, -1, -1, -1]
        temp = False
        for ci, cj in zip(change_i, change_j):
            temp|= self.travel(Pos(cell.i + ci, cell.j + cj), arr)
        return temp

    def isoverlap(self, circle, radius, cell):
        dis = math.pow((circle.i - cell.i), 2) + math.pow((circle.j - cell.j), 2)
        dis = math.sqrt(dis)
        return False if radius < dis else True

    #@param x, y: int -> size of matrix
    #@param N : int -> number of circle
    #@param R : int -> radius
    #@param A : list of int -> x coordinate of circles
    #@param B : list of int -> y coordinate of circles
    def solve(self, X, Y, N, R, A, B):
        arr = [[0 for _ in range(Y + 1)] for _ in range(X + 1)]

        for i in range(X + 1):
            for j in range(Y + 1):
                for cx, cy in zip(A, B):
                    if arr[i][j] != 1:
                        if self.isoverlap(Pos(cx, cy), R, Pos(i, j)):
                            arr[i][j] = 1


        self.n, self.m = X + 1, Y + 1
        if self.travel(Pos(0, 0), arr):
            return "YES"
        else: return "NO"
                
                    


x = 61
y = 91
N = 6
R = 2
A = [ 53, 42, 27, 34, 58, 29 ]
B =  [ 16, 54, 33, 40, 30, 23 ]
t = Solution()
print(t.solve(x, y, N, R, A, B))