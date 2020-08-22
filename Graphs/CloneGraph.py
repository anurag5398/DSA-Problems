"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
"""
#NOT DONE
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def dfs(self, node, visited, path):
        visited.add(node)
        if node.label not in path:
            path[node.label] = []
        for c in node.neighbors:
            path[node.label].append(c.label)
            if c not in visited:
                self.dfs(c, visited, path)

    #@param A : pointer to head of graph
    #@return pointer : cloned graph
    def cloneGraph(self, node):
        path = dict()
        self.dfs(node, set(), path)
        print(path)
        newnode = dict()
        for k in path.keys():
            temp = UndirectedGraphNode(k)
            newnode[k] = temp
        print(newnode)
        for n, neig in path.items():
            for c in neig:
                newnode[n].neighbors.append(newnode[c])
        
        return newnode[node.label]



a = UndirectedGraphNode(1)
b = UndirectedGraphNode(2)
c = UndirectedGraphNode(3)
d = UndirectedGraphNode(4)
e = UndirectedGraphNode(5)
f = UndirectedGraphNode(6)
a.neighbors.append(b)
a.neighbors.append(c)
a.neighbors.append(d)
d.neighbors.append(e)
d.neighbors.append(f)



t = Solution()
a = t.cloneGraph(a)
print("ans")
print(a, a.label, a.neighbors)

        