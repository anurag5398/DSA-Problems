class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
    
class BST:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, root, val):
        if val <= root.val:
            if root.left:
                self.insert(root.left, val)
            else:
                root.left = Node(val)
                return
        elif val > root.val:
            if root.right:
                self.insert(root.right, val)
            else:
                root.right = Node(val)
                return
    
    def insert2(self, root, val):
        if root is None:
            return Node(val)
        
        if val < root.val:
            root.left = self.insert2(root.left, val)
        
        elif val > root.val:
            root.right = self.insert2(root.right, val)

        return root
    
    def maxval(self, root):
        while root.right != None:
            root = root.right
        return root


    def delete(self, root, val):
        if root is None: return root
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            
            temp = self.maxval(root.left)
            root.val = temp.val
            root.left = self.delete(root.left, temp.val)
        return root




    def printtree(self, root):
        if root is None: return
        l, r = None, None
        if root.left: l = root.left.val
        if root.right: r = root.right.val
        print("NODE {} Left {} Right {}".format(root.val, l, r))
        self.printtree(root.left)
        self.printtree(root.right)


a = BST(20) 
a.insert2(a.root, 10)
a.insert2(a.root, 30)
a.insert2(a.root, 5)
a.insert2(a.root, 15)
a.insert2(a.root, 25)
a.insert2(a.root, 35)
a.printtree(a.root)
print("del 30")
a.delete(a.root, 30)
a.printtree(a.root)
print("del 25")
a.delete(a.root, 25)
a.printtree(a.root)



