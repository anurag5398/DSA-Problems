"""
Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.
"""
class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = -1
    
class Trie:
    def __init__(self):
        self.root = Node()
        self.maxxor = 0
        self.val = {'1':'0', '0':'1'}

    def insert(self, string, number):
        self.number = number
        def trieInsert(root, string, i):
            if i == 32:
                root.isEnd = self.number
                return
            else:
                if not string[i] in root.children:
                    root.children[string[i]] = Node()
                trieInsert(root.children[string[i]], string, i+1)
        trieInsert(self.root, string, 0)

    def checkmax(self, string, number):
        self.number = number
        def check(root, string, i):
            if i == 32:
                self.maxxor = max( self.number^root.isEnd , self.maxxor )
                return
            else:
                if self.val[string[i]] in root.children:
                    check(root.children[self.val[string[i]]], string, i+1)
                else:
                    check(root.children[string[i]], string, i+1)
        check(self.root, string, 0)

class Solution:
    def solve(self, A):
        if len(A) <= 1:
            return 0
        trie = Trie()
        for val in A:
            temp = "{:032b}".format(val)
            trie.insert(temp, val)

        for val in A:
            trie.checkmax("{:032b}".format(val), val)
        return trie.maxxor


t = Solution()
A = [5, 17, 100, 11]
print(t.solve(A))
                

    

                    