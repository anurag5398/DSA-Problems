"""
Given an array of words A (dictionary) and another array B (which contain some words).
You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present.
Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if it is not.
Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.
NOTE: Try to do this in O(n) time complexity.
"""

class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = 0
        
class Trie:
    def __init__(self):
        self.root = Node()
        self.ans = 0
    
    def insert(self, string):
        def insert(root, string, i):
            if i == len(string):
                root.isEnd+=1
            else:
                if not string[i] in root.children:
                    root.children[string[i]] = Node()
                insert(root.children[string[i]], string, i+1)
    
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
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        trie = Trie()
        for words in A:
            trie.insert(words)
        print(trie.root.children)
        for i, word in enumerate(B):
            trie.search(word)
            print(word, trie.ans)
            if trie.ans == 0:
                B[i] = 0
            else:
                B[i] = 1
            trie.ans = 0
        return B
            
        
        
        
t = Solution()
A = ["abb","bbb"]
B = ["abb","bbb"]
print(t.solve(A, B))