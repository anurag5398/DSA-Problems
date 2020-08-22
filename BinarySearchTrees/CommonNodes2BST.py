
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None



def solve(A, B):
    s1, s2 = [], []
    ans = 0
    while True:
        if A:
            s1.append(A)
            A = A.left
        elif B:
            s2.append(B)
            B = B.left
        elif s1[-1] == s2[-1]:
            ans+= s1[-1]
            x = s1.pop()
            y = s2.pop()
            A = x.right
            B = y.right
        elif s1[-1] < s2[-1]:
            x = s1.pop()
            A = x.right
        elif s1[-1] > s2[-1]:
            y = s2.pop()
            B = y.right()
        else:
            break
    print(ans)
    return ans



a = Node(5)
b = Node(3)
c = Node(10)
d = Node(1)
e = Node(4)
f = Node(15)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

for i in inorder(a):
    print(i.next)


