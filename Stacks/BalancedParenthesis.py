"""
Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.
"""
class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, val):
        self.stack.append(val)
        self.count+=1
    def pop(self):
        if self.count < 0:
            return None
        else:
            temp = self.stack.pop()
            self.count-=1
            return temp
    def top(self):
        if self.count < 0:
            return None
        else:
            self.stack[self.count]

class Solution:
    def __init__(self):
        self.normal = Stack()
        self.curly = Stack()
        self.square = Stack()
    def solve(self, A):
        for i in A:
            if i == '(':
                self.normal.push('(')
            elif i == ')':
                temp = self.normal.pop()
                if temp is None:
                    return 0
            elif i == '{':
                self.curly.push('{')
            elif i == '}':
                temp = self.curly.pop()
                if temp is None:
                    return 0
            elif i == '[':
                self.square.push('[')
            elif i == ']':
                temp = self.square.pop()
                if temp is None:
                    return 0
        if self.normal.count == -1 and self.curly.count == -1 and self.square.count == -1:
            return 1
        else:
            return 0

test = Solution()
print(test.solve("(anu)[r]ag"))