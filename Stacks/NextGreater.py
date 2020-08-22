"""
Given an array, A find the next greater element G[i] for every element A[i] in the array. The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array, A.
More formally:
G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]
Elements for which no greater element exist, consider next greater element as -1.
"""
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
            return self.stack.pop()
        else:
            return None
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return None

class Solution:
    def nextGreater(self, A):
        stack = Stack()
        for i in range(len(A)-1,-1,-1):
            while stack.count > -1 and stack.top() <= A[i]:
                stack.pop()
            if stack.count == -1:
                stack.push(A[i])
                A[i] = -1
            elif stack.top() > A[i]:
                temp = A[i]
                A[i] = stack.top()
                stack.push(temp)
        return A


test = Solution()
print(test.nextGreater([4,7,3,8]))
                
