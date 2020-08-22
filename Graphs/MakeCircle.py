"""
Given an array of strings A of size N, find if the given strings can be chained to form a circle.
A string X can be put before another string Y in circle if the last character of X is same as first character of Y.
NOTE: All strings consist of lower case characters.
"""
#in one dfs from any word, all the other words should be covered
#and each node has indegree == outdegree    


class Solution:
    def dfs(self, node, visited, adj):
        visited.add(node)
        for c in adj[node]:
            if c not in visited:
                self.dfs(c, visited, adj)
            else:
                if len(visited) == len(adj):
                    self.allvisited = True
    def adddict(self, v, tempdict):
        if v in tempdict:
            tempdict[v]+=1
        else:
            tempdict[v] = 1
    def adddictval(self, w, adj):
        if w[0] in adj: adj[w[0]].append(w[-1])
        else: adj[w[0]] = [w[-1]]
        if w[-1] not in adj:
            adj[w[-1]] = []
    #@param A : list of string
    #@return int : 1/0
    def solve(self, A):
        adj = dict()
        _in, _out = dict(), dict()
        for w in A:
            self.adddictval(w, adj)
            self.adddict(w[0], _out)
            self.adddict(w[-1], _in)
        same = True
        if _out != _in: return 0
        self.allvisited = False
        self.dfs(A[0][0], set(), adj)
        return 1 if self.allvisited else 0
        

            
            




t = Solution()
A = [ "zaz", "zbz", "zaz", "zdz" ]
print(t.solve(A))