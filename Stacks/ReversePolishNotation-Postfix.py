class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self,val):
        self.count+=1
        self.stack.append(val)
    def pop(self):
        if self.count > -1:
            self.count-=1
            return self.stack.pop()
        else:
            return None
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return None

class Solution:
    def __init__(self):
        self.stack = Stack()
    def solve(self, inputlist):
        for val in inputlist:
            if val == '+':
                if self.stack.count < 1:
                    return -1
                var2 = int(self.stack.pop())
                var1 = int(self.stack.pop())
                self.stack.push(var1+var2)
            elif val == '-':
                if self.stack.count < 1:
                    return -1
                var2 = int(self.stack.pop())
                var1 = int(self.stack.pop())
                self.stack.push(var1-var2)
            elif val == '*':
                if self.stack.count < 1:
                    return -1
                var2 = int(self.stack.pop())
                var1 = int(self.stack.pop())
                self.stack.push(var1*var2)
            elif val == '/':
                if self.stack.count < 1:
                    return -1
                var2 = int(self.stack.pop())
                var1 = int(self.stack.pop())
                self.stack.push(var1//var2)
            else:
                self.stack.push(val)

        return self.stack.top()
                

test = Solution()
print(test.solve(["4", "13", "5", "/", "+"]))