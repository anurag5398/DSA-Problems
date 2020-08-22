"""
Given two arrays of strings A of size N and B of size M.
Return a binary string C where C[i] = '1' if B[i] can be found in dictionary A using exactly one modification in B[i], Else C[i] = '0'.
NOTE: modification is defined as converting a character into another character.
"""

class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.temp = False

    def insert(self, string):
        def trieInsert(root, string, i):
            if i == len(string):
                root.isEnd = True
            else:
                if not string[i] in root.children:
                    root.children[string[i]] = Node()
                trieInsert(root.children[string[i]], string, i+1)
        trieInsert(self.root, string, 0)
    
    def modifiedSearch(self, string):
        def test(root, string, i, replacement):
            if i == len(string):
                if replacement and root.isEnd:
                    self.temp = True
                    return
            else:
                if not replacement:
                    for k in root.children.keys():
                        if k != string[i]:
                            test(root.children[k], string, i+1, True)
                if string[i] not in root.children: return
                test(root.children[string[i]], string, i+1, replacement)
        test(self.root, string, 0, False)

class Solution:
    def solve(self, A, B):
        trie = Trie()
        for word in A:
            trie.insert(word)

        ans = ""
        for pword in B:
            trie.modifiedSearch(pword)
            if trie.temp: ans+= "1"
            else: ans+= "0"
            trie.temp = False
        return ans



t = Solution()
A = ["data", "circle", "cricket"]
B = ["date", "circel", "crikket", "data", "circl"]
print(t.solve(A, B))