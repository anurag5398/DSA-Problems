"""
Given a list of N words. Find shortest unique prefix to represent each word in the list.
NOTE: Assume that no word is prefix of another. In other words, the representation is always possible
"""

class Node:
    def __init__(self):
        self.children = dict()
        self.iscount = 0

class Trie:
    def __init__(self):
        self.root = Node()
        self.ans = ""
    
    def insert(self, string):
        def insert(root, string, i):
            if i == len(string): return
            else:
                if not string[i] in root.children:
                    root.children[string[i]] = Node()
                root.iscount+=1
                insert(root.children[string[i]], string, i+1)
        insert(self.root, string, 0)
    
    def uprefix(self, string):
        def uprefix(root, string, i):
            if i == len(string): return
            if root.iscount == 1: return
            else: self.ans+= string[i]
            #print("root children {}".format(root.children))
            uprefix(root.children[string[i]], string, i+1)
        uprefix(self.root, string, 0)



class Solution:
    def prefix(self, A):
        trie = Trie()
        for i in A:
            trie.insert(i)
        for i, word in enumerate(A):
            trie.uprefix(word)
            A[i] = trie.ans
            trie.ans = ""
        return A

t = Trie()
t.insert("dove")
t.insert("dog")
t.uprefix("dove")
print(t.ans)

re = Solution()
A = ['bearcat','bert','dove','duck']
print(re.prefix(A))
