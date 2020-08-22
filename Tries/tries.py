#trie DS

class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, root, string, i):
        if i == len(string):
            root.isEnd = True
        else:
            if not string[i] in root.children:
                root.children[string[i]] = Node()
            self.insert(root.children[string[i]], string, i+1)
    

    def search(self, root, string, i):
        if i == len(string):
            if root.isEnd: print("found")
            else: print("Not Found")
        else:
            if string[i] in root.children:
                self.search(root.children[string[i]], string, i+1)
            else:
                return False

    def delete(self, root, string, i):
        if i == len(string):
            if root.isEnd: root.isEnd = False
            else: print("Not found for Deletion")
        else:
            if string[i] in root.children:
                #print("string[i] {} len root.chil {} root.chil[str[i]] {} isEnd {}".format( string[i], len(root.children), len(root.children[string[i]].children), root.children[string[i]].isEnd ))
                self.delete(root.children[string[i]], string, i+1)
                if len(root.children[string[i]].children) == 0:
                    if root.children[string[i]].isEnd: return
                    root.children.pop(string[i])
            else:
                print("Not found for Deletion")
                return
    
    
    
    def printlvl(self, root):
        print(root.children)
    
    

a = Trie()
a.insert(a.root, "amul", 0)
a.insert(a.root, "amulya", 0)
a.delete(a.root, "amul", 0)
a.search(a.root, "amulya", 0)

a.insert(a.root, "b", 0)
a.search(a.root, "b", 0)
