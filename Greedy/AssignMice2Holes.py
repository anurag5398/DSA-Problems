"""
There are N Mice and N holes that are placed in a straight line. Each hole can accomodate only 1 mouse.
The positions of Mice are denoted by array A and the position of holes are denoted by array B.
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1. Any of these moves consumes 1 minute.
Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.
"""
class Solution:
    #@param A : list of int -> position of mice
    #@param B : list of int -> position of holes
    #@return an int -> time for last mice to reah hole
    def solve(self, A, B):
        A, B = sorted(A), sorted(B)
        maxtime = 0
        for i, j in zip(A, B):
            maxtime = max(abs(i-j), maxtime)
        return maxtime

t = Solution()
A = [-6]
B = [-2]
print(t.solve(A, B))