"""
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.
Chech whether A has redundant braces or not.
NOTE: A will be always a valid expression.
1 - is redundant, 0 - correct
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, value):
        self.stack.append(value)
        self.count+=1
    def pop(self):
        if self.count < 0:
            return -1
        else:
            temp = self.stack.pop()
            self.count-=1
            return temp
    def top(self):
        if self.count < 0:
            return -1
        else:
            return self.stack[self.count]
    def printstack(self):
        print(self.stack)

class Solution:
    def __init__(self):
        self.balanced = Stack()
    #eg.   (a + (a + b))
    def braces(self, A):
        for char in A:

            if char == "+" or char == "-" or char == "*" or char == "/" or char == "(":
                self.balanced.push(char)
            elif char == ")":
                found = False
                temp = self.balanced.pop()
                while temp != "(" and temp != -1:
                    #print("char {} temp {} stack {}".format(char, temp, self.balanced.printstack()))
                    if temp == "+" or temp == "-" or temp == "*" or temp == "/":
                        found = True
                    temp = self.balanced.pop()
                
                if temp == "(":
                    if not found:
                        return 1
                else:
                    return 1
        return 0

test = Solution()
print(test.braces("((a + b))"))
        
