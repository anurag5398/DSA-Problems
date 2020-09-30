"""
A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.
Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.
All students who know each other are placed in one batch.
Strength of a batch is equal to sum of the strength of all the students in it.
Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.
Find the number of batches selected.
NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.
"""
from collections import defaultdict
class Solution:
    #@param visited: set
    #@param node: int
    def dfs(self, visited: set, node: int):
        visited.add(node)
        self.tempsum+=self.B[node - 1]
        for c in self.edges[node]:
            if c not in visited:
                self.dfs(visited, c)

    #@param A: int
    #@param B: list of int
    #@param C: list of list of int
    #@param D: int
    #@return an int
    def solve(self, A: int, B: list, C: list, D: int) -> int:
        self.B = B
        self.edges = defaultdict(list)
        for s, d in C:
            self.edges[s].append(d)
            self.edges[d].append(s)
        visited = set()
        ans = 0

        for node in range(1, A + 1):
            if node not in visited:
                self.tempsum = 0
                self.dfs(visited, node)
                if self.tempsum >= D: ans+=1
        return ans




A = 5
B = [1, 2, 3, 4, 5]
C = [  [1, 5],
        [2, 3]  ]
D = 6

t = Solution()
print(t.solve(A, B, C, D))