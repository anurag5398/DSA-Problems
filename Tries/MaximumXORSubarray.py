"""
Given an array A of integers of size N. Find the subarray AL, AL+1, AL+2, ... AR with 1<=L<=R<=N which has maximum XOR value.
NOTE: If there are multiple subarrays with same maximum value, return the subarray with minimum length. If length is same, return the subarray with minimum starting index.
"""

class Node:
    def __init__(self):
        self.children = dict()
        self.number = -1
        self.index = -1
    
class Trie:
    def __init__(self):
        self.root = Node()
        self.reverse = {'0':'1', '1':'0'}
        self.maxxor = -1
        self.ans = (-1, -1)

    def insert(self, number, index):
        self.number, self.index = number, index
        binString = "{:032b}".format(number)
        def trieInsert(root, string, i):
            if i == 32:
                root.number = self.number
                root.index = self.index
                return
            else:
                if not string[i] in root.children:
                    root.children[string[i]] = Node()
                trieInsert(root.children[string[i]], string, i+1)
        trieInsert(self.root, binString, 0)

    def setanswer(self, one , two):
        if one <= two: self.ans = (one, two)
        else: self.ans = (two, one)
        return

    def findmax(self, number, index):
        self.number, self.index = number, index
        binString = "{:032b}".format(number)
        def find(root, string, i):
            if i == 32:
                if self.number^root.number > self.maxxor:
                    self.maxxor = self.number^root.number
                    self.setanswer(self.index, root.index)
                elif self.number^root.number == self.maxxor:
                    if abs(root.index-self.index) < (self.ans[1]-self.ans[0]):
                        self.setanswer(self.index, root.index)
                return
            else:
                if self.reverse[string[i]] in root.children:
                    find(root.children[self.reverse[string[i]]], string, i+1)
                else:
                    find(root.children[string[i]], string, i+1)
        find(self.root, binString, 0)


class Solution:
    def solve(self, A):
        trie = Trie()

        temp = 0
        for i, val in enumerate(A):
            temp = temp^val
            A[i] = temp

        for i, val in enumerate(A):
            trie.insert(val, i+1)

        A.insert(0, 0)
        for i, val in enumerate(A):
            trie.findmax(val, i)

        return trie.ans[0]+1,trie.ans[1]

A = [1,4,3,7,10]

t = Solution()
t.solve(A)


        
