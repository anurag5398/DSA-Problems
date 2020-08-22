"""
Given a list of N words denoted by string array A of size N.
You have to answer Q queries denoted by string array B, for each query you have a string S of size M, find the number of words in the list A which have string S as a prefix and suffix.
NOTE: The size M for all strings in the queries remains same.
"""

class Node:
    def __init__(self):
        self.children = dict()
        self.endCount = 0

class Trie:
    def __init__(self):
        self.root = Node()
        self.ans = 0
    
    def insert(self, string):
        def insert(root, string, i):
            if i == len(string):
                root.endCount+=1
                return
            if not string[i] in root.children:
                root.children[string[i]] = Node()
            insert(root.children[string[i]], string, i+1)
        insert(self.root, string, 0)

    def search(self, string):
        def search(root, string, i):
            if i == len(string):
                self.ans = root.endCount
                return
            else:
                if string[i] in root.children:
                    search(root.children[string[i]], string, i+1)
        search(self.root, string, 0)


class Solution:
    def check(self, word, m):
        size = len(word)
        for i in range(m):
            j = size - m + i
            if word[i] != word[j]:
                return False
        return True

    def solve(self, A, B):
        m = len(B[0])
        trie = Trie()
        for word in A:
            if self.check(word, m):
                trie.insert(word[0:m])
        
        for i, pre in enumerate(B):
            trie.search(pre)
            B[i] = trie.ans
            trie.ans = 0
        return B
                
                
t = Solution()
A = ["ababa", "aabbvaab", "aecdsaaec", "abaaxbqaba"]
B = ["aba", "aec", "abb", "aab"]
t.solve(A, B)