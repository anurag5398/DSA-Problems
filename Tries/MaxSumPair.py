"""
Rishabh was sitting ideally in his office and then suddenly his boss gave him some operations to perform.
You being his friend tried to help him in finishing the task fast.
So you have to perform Q operation of two types:
Operation 1: INSERT : You are given an pair of (string, integer).The string represents the key and the integer represents the value. Insert the key-value pair in the hash and If the key already exists in hash, then the original key-value pair will be overridden to the new one.
Operation 2: SUM : you'll be given an pair of (string, -1) where string representing the prefix, and you need to return the sum of all the pairs' value in the hash whose key starts with the prefix.
"""

class Node:
    def __init__(self):
        self.children = dict()
        self.endVal = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word, val):
        self.val = val
        def addword(i, root, word):
            if i == len(word):
                root.endVal = self.val
            else:
                if not word[i] in root.children:
                    root.children[word[i]] = Node()
                addword(i + 1, root.children[word[i]], word)
        addword(0, self.root, word)

    def findSum(self, pref):
        self.total = 0
        def parseSum(root):
            for k, node in root.children.items():
                self.total+= node.endVal
                parseSum(node)
                

        def find(i, root, word):
            if i == len(word):
                parseSum(root)
            else:
                if word[i] in root.children:
                    find(i + 1, root.children[word[i]], word)
                else: return
        find(0, self.root, pref)
        return self.total

class Solution:
    def solve(self, A: list, B: list) -> list:
        trie = Trie()
        ans = list()
        for word, val in zip(A, B):
            if val == -1:
                ans.append(trie.findSum(word))
            else:
                trie.insert(word, val)
        return ans

t = Solution()
A = ["apple", "ap", "apple", "ap"]
B = [3, -1, 1, -1]
print(t.solve(A, B))

                