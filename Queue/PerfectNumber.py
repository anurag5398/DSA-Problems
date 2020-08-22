"""
Given an integer A, you have to find the Ath Perfect Number.
A Perfect Number has the following properties:
It comprises only 1 and 2.
The number of digits in a Perfect number is even.
It is a palindrome number.
For example 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.
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
        queue = Queue(A)
        queue.enqueue(1)
        queue.enqueue(2)
        count = 0
        while True:
            temp = queue.dequeue()
            count+=1
            if count == A:
                ans = str(temp)
                ans+= ans[len(ans)-1::-1]
                return ans
            queue.enqueue(temp*10+1)
            queue.enqueue(temp*10+2)

test = Solution()
print(test.solve(130))
