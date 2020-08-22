"""
You are given a string A.
An operation on the string is defined as follows:
Remove the first occurrence of same consecutive characters. eg for a string "abbcd", the first occurrence of same consecutive characters is "bb".
Therefore the string after this operation will be "acd".
Keep performing this operation on the string until there are no more occurrences of same consecutive characters and return the final string.
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
            self.count-=1
            return self.stack.pop()
        else:
            return "0"
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return "0"
    def returnstack(self):
        #print(self.stack)
        return "".join(self.stack)

class Solution:
    def solve(self, A):
        temp = Stack()
        for i in A:
            if temp.top() == i:
                temp.pop()
            else:
                temp.push(i)
        a = temp.returnstack()
        return a

test = Solution()
print(test.solve("abbabb"))
        