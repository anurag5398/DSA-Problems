"""
Given an array of integers A .
A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1.
Find the area of the largest rectangle formed by the histogram.
"""
#approch - for each bar find the first smallest on left and right

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
            return None
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return None

class Solution:
    def __init__(self):
        self.stack = Stack()
        self.stack2 = Stack()
    def largestRectangleArea(self, A):
        size = len(A)
        ls, rs = [None]*size, [None]*size

        for i in range(size):
            while self.stack.count > -1 and A[self.stack.top()] >= A[i]:
                self.stack.pop()
            if self.stack.count <= -1:
                ls[i] = -1
                self.stack.push(i)
            if A[self.stack.top()] < A[i]:
                ls[i] = self.stack.top()
                self.stack.push(i)

            j = size-i-1
            while self.stack2.count > -1 and A[self.stack2.top()] >= A[j]:
                self.stack2.pop()
            if self.stack2.count <= -1:
                rs[j] = size
                self.stack2.push(j)
            if A[self.stack2.top()] < A[j]:
                rs[j] = self.stack2.top()
                self.stack2.push(j)
        print(ls)
        print(rs)
        maxarea = 0
        for i in range(size):
            maxarea = max(A[i]*(rs[i]-ls[i]-1), maxarea)
        return maxarea

A = [90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]
test = Solution()
print(test.largestRectangleArea(A))
            