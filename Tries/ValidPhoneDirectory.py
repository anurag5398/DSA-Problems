"""
Given a phone directory in the form of string array A containing N numeric strings.
If any phone number is prefix of another phone number then phone directory is invalid else it is valid.
You need to check whether the given phone directory is valid or not if it is valid then return 1 else return 0.
"""
class Node:
    def __init__(self):
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, root: Node, string: str, i: int):
        if i == len(string) - 1:
            if string[i] in root.children:
                self.dupl = True
            else:
                root.children[string[i]] = Node()
        else:
            if not string[i] in root.children:
                root.children[string[i]] = Node()
            self.insert(root.children[string[i]], string, i + 1)

class Solution:
    def solve(self, A: list):
        trie = Trie()
        trie.dupl = False
        for no in A:
            trie.insert(trie.root, no, 0)
            if trie.dupl is True: return 0
        return 1


t = Solution()
A = ["00121", "001"]
print(t.solve(A))

