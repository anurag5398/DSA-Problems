class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, val):
        self.count+=1
        self.stack.append(val)
    def pop(self):
        if self.count > -1:
            self.count-=1
            return self.stack[self.count+1]
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
    def printstack(self):
        print(self.stack)

class Solution:
    def solve(self, A , B):
        stack = Stack()
        if B > len(A):
            return None
        for i in range(B):
            stack.push(A[i])

        stack.printstack()
        print(stack.top())
        print(st)
        i = 0
        while stack.count > -1:
            A[i] = stack.pop()
            i+=1

        return A

test = Solution()
A = [1, 2,3, 4, 5]
print(test.solve(A, 3))
