"""
Given an integer A. Find and Return first positive A integers in ascending order containing only digits 1, 2 and 3.
NOTE: All the A integers will fit in 32 bit integer.
"""

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*self.size
        self.r , self.f = -1, -1

    def enqueue(self, val):
        if (self.f == self.r != -1) or (self.f == -1 and self.r == self.size-1):
            #print("Full")
            return None
        else:
            self.r = (self.r + 1)%self.size
            self.queue[self.r] = val
    
    def dequeue(self):
        if self.r == self.f == -1:
            #print("Empty")
            return None
        else:
            self.f = (self.f + 1)%self.size
            temp = self.queue[self.f]
            if self.f == self.r:
                self.r, self.f = -1, -1
            return temp
    def front(self):
        if self.r == self.f == -1:
            #print("Empty")
            return None
        else:
            return self.queue[(self.f+1)%self.size]

class Solution:
    def solve(self, A):
        queue = Queue(2*A)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        count = 0
        ans = []
        while True:
            temp = queue.dequeue()
            count+=1
            ans.append(temp)
            if count == A:
                return ans
            
            queue.enqueue(temp*10 + 1)
            queue.enqueue(temp*10 + 2)
            queue.enqueue(temp*10 + 3)

test = Solution()
print(test.solve(7))
