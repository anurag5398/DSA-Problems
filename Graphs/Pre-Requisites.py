"""
There are a total of A courses you have to take, labeled from 1 to A.
Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].
So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses
"""
#since order is not required
#we can just check if the graph has any loops
#if there is a loop then studying all is no possible

from collections import defaultdict
#topological sort
class Solution:
    def solve(self, A, B, C):
        inDegree, outDegree = dict(), defaultdict(list)
        for i in range(1, A + 1): inDegree[i] = 0
        for s, d in zip(B, C):
            outDegree[s].append(d)
            inDegree[d]+=1
        
        stack = list()
        for k, v in inDegree.items():
            if v == 0:
                stack.append(k)
                
                

        while stack:
            temp = stack.pop()
            inDegree.pop(temp)
            for c in outDegree[temp]:
                inDegree[c]-=1
                if inDegree[c] == 0:
                    stack.append(c)
        
        if len(inDegree) == 0: return 1
        return 0
            
            
        return 1

class Solution2:
    def dfs(self, node, visited, pathVisited, edges):
        visited[node] = True
        pathVisited[node] = True

        for c in edges[node]:
            if visited[c] == False:
                if self.dfs(c, visited, pathVisited, edges):
                    return True
            elif pathVisited[c] == True:
                return True
        
        pathVisited[node] = False
        return

    def solve(self, A, B, C):
        edges = defaultdict(list)
        for s, d in zip(B, C):
            edges[s].append(d)
        
        visited = [False] * (A + 1)
        pathVisited = [False] * (A + 1)
        for i in range(1, A + 1):
            if i not in visited:
                if self.dfs(i, visited, pathVisited, edges):
                    return 0
        return 1
            

                

t = Solution()
A = 3
B = [1, 2]
C = [2, 3]
print(t.solve(A, B, C))