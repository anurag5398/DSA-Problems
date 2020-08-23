"""
Given the number of vertices A in a Cyclic Graph.
Your task is to determine the number of colors required to color the graph so that no two Adjacent vertices have the same color.
"""
#as per examples, question is refering to simple cyclic graph
#it has one cycle, so depending on odd/even number of nodes
#we can use 2 or 3 colors



class Solution:
    #@param A : int
    #@return int
    def solve(self, A):
        if A == 1: return 1
        if A%2 == 0: return 2
        return 3