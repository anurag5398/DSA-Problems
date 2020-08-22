"""
You are given n towns (1 to n). All towns are connected via unique directed path as mentioned in the input.
Given 2 towns find whether you can reach the first town from the second without repeating any edge.
x y : query to find whether x is reachable from y.
Input contains an integer array A of size n and 2 integers x and y ( 1 <= x, y <= n ).
There exist a directed edge from A[i] to i+1 for every 1 <= i < n. Also, it's guaranteed that A[i] <= i.
NOTE: Array A is 0-indexed.
"""
#question seems fishy

class Solution:
    #@param A : list of int
    #@param B : int
    #@param C : int
    #@return int -> 1/0
    def solve(self, A, B, C):
        self.B = B
        path = dict()
        for i in range(1, len(A) + 1): path[i] = list()
        for i, v in enumerate(A): path[v].append(i + 1)
        
        def dfs(node, visited, adjList):
            if node == self.B: return True
            visited.add(node)
            temp = False
            for c in adjList[node]:
                if c not in visited:
                    temp|= dfs(c, visited, adjList)
            return temp

        return 1 if dfs(C, set(), path) else 0 
            

t = Solution()
A = [ 1, 1, 1, 3, 3, 2, 2, 7, 6 ]
B = 9
C = 1
print(t.solve(A, B, C))