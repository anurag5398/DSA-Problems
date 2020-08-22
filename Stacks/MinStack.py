"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:

All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty."""

class MinStack:
    def __init__(self):
        self.stack = []
        self.scount = -1
        self.minstack = []
        self.mcount = -1
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if self.scount == -1 or x <= self.minstack[self.mcount]:
            self.minstack.append(x)
            self.mcount+=1
        self.scount+=1
        self.stack.append(x)
        
    # @return nothing
    def pop(self):
        if self.scount > -1:
            if self.minstack[self.mcount] == self.stack[self.scount]:
                self.minstack.pop()
                self.mcount-=1
            self.stack.pop()
            self.scount-=1
            
        

    # @return an integer
    def top(self):
        if self.mcount <= -1:
            return -1
        else:
            return self.stack[self.scount]
        

    # @return an integer
    def getMin(self):
        if self.mcount <= -1:
            return -1
        else:
            return self.minstack[self.mcount]
        
        
