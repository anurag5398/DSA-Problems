"""
Given an array of integers A. Find and return the number of subarrays whose xor values is less than B.
NOTE: As the answer can be very large, return the answer modulo (109+7).
"""
class Node:
    def __init__(self):
        self.children = dict()
        self.count = 0
        self.isEnd = -1

class Trie:
    def __init__(self):
        self.root = Node()
        self.rev = {'0':'1', '1':'0'}

    def insert(self, val):
        number = "{:022b}".format(val)
        self.val = val
        def trieInsert(root, number, i):
            if i == len(number):
                root.isEnd = self.val
                return
            else:
                if not number[i] in root.children:
                    root.children[number[i]] = Node()
                root.children[number[i]].count+=1
                trieInsert(root.children[number[i]], number, i+1)
        trieInsert(self.root, number, 0)
                
    def search(self, val):
        number = "{:022b}".format(val)
        self.ans = 0
        def check(root, A, i):
            if i == len(A): return
            else:
                if self.B[i] == '0':
                    if A[i] in root.children:
                        check(root.children[A[i]], number, i+1)
                elif self.B[i] == '1':
                    if A[i] in root.children:
                        self.ans+= root.children[A[i]].count
                    if self.rev[A[i]] in root.children:
                        check(root.children[self.rev[A[i]]], number, i+1)
        check(self.root, number, 0)
        return self.ans


class Solution:
    def solve(self, A, B):
        temp = 0
        for i, val in enumerate(A):
            temp^= val
            A[i] = temp

        t = Trie()
        t.B = "{:022b}".format(B)
        total = 0
        t.insert(0)

        for no in A:
            total+= t.search(no)
            t.insert(no)
        
        return total
    

t = Solution()
A = [ 5, 3, 10, 12, 5, 14, 4, 7, 4 ]
B = 4

print(t.solve(A,B))
