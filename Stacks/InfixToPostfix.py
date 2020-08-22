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
    def solve(self, A):
        stack = Stack()
        ans = ""
        for i in range(len(A)):
            if A[i].isalpha():
                ans+= A[i]
            
            elif A[i] == '+' or A[i] == '-':
                while stack.count > -1 and (stack.top() == '+' or stack.top() == '-' or stack.top() == '*' or stack.top() == '/' or stack.top() == '^'):
                    temp = stack.pop()
                    ans+= temp
                stack.push(A[i])
            
            elif A[i] == '*' or A[i] == '/':
                while stack.count > -1 and (stack.top() == '*' or stack.top() == '/' or stack.top() == '^'):
                    temp = stack.pop()
                    ans+= temp
                stack.push(A[i])

            elif A[i] == '^':
                while stack.count > -1 and stack.top() == '^':
                    temp = stack.pop()
                    ans+= temp
                stack.push(A[i])

            elif A[i] == '(':
                stack.push(A[i])
            
            elif A[i] == ')':
                while stack.count > -1 and stack.top() != '(':
                    temp = stack.pop()
                    ans+= temp
                stack.pop()
        while stack.count > -1:
            ans+= stack.pop()
        return ans

test = Solution()
string = "a+b*(c^d-e)^(f+g*h)-i"
print(test.solve(string))