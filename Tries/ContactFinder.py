"""
We want to make a custom contacts finder applications as part of our college project. The application must perform two types of operations:
Type 1: Add name B[i] ,denoted by 0 in vector A where B[i] is a string in vector B denoting a contact name. This must store B[i] as a new contact in the application.
Type 2: Find partial for B[i] ,denoted by 1 in vector A where B[i] is a string in vector B denoting a partial name to search the application for. It must count the number of contacts starting with B[i].
You have been given sequential add and find operations. You need to perform each operation in order.
And return as an array of integers, answers for each query of type 2(denoted by 1 in A) .
"""

class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, string):
        def trieInsert(root, string, i):
            if i == len(string):
                root.isEnd+=1
            else:
                if not string[i] in root.children:
                    root.children[string[i]] = Node()
                trieInsert(root.children[string[i]], string, i+1)
        trieInsert(self.root, string, 0)

    def test(self, string):
        def realtest(root, string, i):
            if self.found == False: return
            if i < len(string):
                if string[i] in root.children:
                    realtest(root.children[string[i]], string, i+1)
                    #print(string[i])
                else:
                    self.found = False
                    return   
            else:
                #print("End ",root.isEnd)
                self.count+= root.isEnd
                for k in root.children.keys():
                    realtest(root.children[k], string, i+1)
        realtest(self.root, string, 0)


class Solution:
    def solve(self, A, B):
        trie = Trie()
        ans = []
        trie.found = True
        trie.count = 0
        for q, word in zip(A, B):
            if q == 0:
                trie.insert(word)
            elif q == 1:
                trie.test(word)
                ans.append(trie.count)
                trie.found = True
                trie.count = 0
        return ans

    


s = Solution()
A = [0, 1]
B = ["abcde", "abc"]
print(s.solve(A, B))