"""
Given a stack of integers A, sort it using another stack.
Return the array of integers after sorting the stack using another stack.
"""
class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, val):
        self.stack.append(val)
        self.count+=1
    def pop(self):
        if self.count > -1:
            temp = self.stack.pop()
            self.count-=1
            return temp
        return -1
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        return -1
    def isempty(self):
        if self.count < 0:
            return True
        return False

class Solution:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    def solve(self, A):
        for i in A:
            if self.stack1.isempty():
                self.stack1.push(i)
            elif i >= self.stack1.top():
                self.stack1.push(i)
            elif i < self.stack1.top():
                while self.stack1.count > -1 and self.stack1.top() > i:
                    temp = self.stack1.pop()
                    self.stack2.push(temp)
                self.stack1.push(i)
                while self.stack2.isempty() is False:
                    temp = self.stack2.pop()
                    self.stack1.push(temp)
        return self.stack1.stack

A = [5, 17, 100, 11, 150, 2, 1, 28]
test = Solution()
test.solve(A)
    
