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
    def prevSmaller(self, A):
        ans = [None]*len(A)
        for i in range(len(A)):
            while self.stack.count > -1 and self.stack.top() >= A[i]:
                self.stack.pop()
            if self.stack.count <= -1:
                ans[i] = -1
                self.stack.push(A[i])
            if self.stack.top() < A[i]:
                ans[i] = self.stack.top()
                self.stack.push(A[i])
        return ans

test = Solution()
print(test.prevSmaller([3, 2, 1]))