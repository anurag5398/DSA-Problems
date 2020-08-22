"""
A CPU has N tasks to be performed. It is to be noted that the tasks have to be performed in a specific order to avoid deadlock. In every clock cycle the CPU can either perform a task or move it to the back of the queue. You are given the current state of the scheduler queue in an array A and the required order of the tasks in an array B.
Determine the minimum number of clock cycles to complete all the tasks.
"""

import time
A = [2, 3, 1, 5, 4]
B = [1, 3, 5, 4, 2]


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
    def top(self):
        if self.count > -1:
            return self.stack[self.count]

class Solution:
    def solve(self, A, B):
        task = Stack()
        size = len(A)

        for i in range(len(B)-1, -1, -1):
            task.push(B[i])

        i, count = 0, 0
        while task.count > -1:
            if A[i] == None:
                i = (i + 1)%size
            elif A[i] != task.top():
                i = (i + 1)%size
                count+=1
            elif A[i] == task.top():
                task.pop()
                A[i] = None
                i = (i + 1)%size
                count+=1
        return count

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*self.size
        self.f, self.r = -1, -1

    def enqueue(self, val):
        if (self.f == self.r != -1) or (self.f == -1 and self.r == self.size-1):
            print("full")
            return "Full"
        else:
            self.r = (self.r + 1)%self.size
            self.queue[self.r] = val

    def dequeue(self):
        if self.f == self.r == -1:
            print("empty")
            return "Empty"
        else:
            self.f = (self.f + 1)%self.size
            if self.f == self.r:
                self.f, self.r = -1, -1
    def front(self):
        if self.f == self.r == -1:
            print("empty")
            return "Empty"
        else:
            return self.queue[(self.f+1)%self.size]
    

class BetterSolution:
    def solve(self, A, B):
        task = Stack()
        order = Queue(10)

        for i in range(len(B)-1, -1, -1):
            task.push(B[i])

    
        for i in range(len(A)):
            order.enqueue(A[i])

        #print("task top {} order front {}".format(task.top(), order.front()))

        i, count = 0, 0
        while task.count > -1:
            #time.sleep(2)
            #print("task top {} order front {}".format(task.top(), order.front()))
            if order.front() == task.top():
                order.dequeue()
                task.pop()
                count+=1
            else:
                temp = order.front()
                order.dequeue()
                order.enqueue(temp)
                count+=1
            
        return count

        


#test = Solution()
test2 = BetterSolution()
#print(test.solve(A, B))
print(test2.solve(A, B))