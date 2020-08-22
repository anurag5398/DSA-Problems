"""
Given an integer array A of size N. You have to generate it's all subarrays having the size greater than 1.
Then for each subarray find Bitwise XOR of its maximum and second maximum element.
Find and return the maximum value of XOR among all subarrays.
"""
"""
Approch: Consider stack element as 2nd max. So until a greater no is reached than top, push. (Consider each element to be 2nd max and find the first max)(from both sides)
"""
#instead of stack class, can use array in solution directly -> top = arr[-1]

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
        return None
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return None
    def isempty(self):
        if self.count > -1:
            return False
        else:
            return True

class Solution:
    def __init__(self):
        self.stack = Stack()
        self.stackright = Stack()
    def solve(self, A):
        n, maxxor = len(A), 0
        for i,val in enumerate(A):
            if self.stack.isempty() or val <= self.stack.top():
                self.stack.push(val)
            elif val > self.stack.top():
                while self.stack.count > -1 and val > self.stack.top():
                    maxxor = max(val^self.stack.top(), maxxor)
                    self.stack.pop()
                self.stack.push(val)
            
            #reverse check
            val2 = A[n-i-1]
            if self.stackright.isempty() or val2 <= self.stackright.top():
                self.stackright.push(val2)
            elif val2 > self.stackright.top():
                while self.stackright.count > -1 and val2 > self.stackright.top():
                    maxxor = max(val2^self.stackright.top(), maxxor)
                    self.stackright.pop()
                self.stackright.push(val2)
        return maxxor


A = [7, 2, 5, 1, 4, 3, 6, 11, 2]
test = Solution()
print(test.solve(A))
