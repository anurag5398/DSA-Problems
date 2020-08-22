"""
Given an array A of both positive and negative integers.
Your task is to compute sum of minimum and maximum elements of all sub-array of size B.
NOTE: Since the answer can be very large, you are required to return the sum modulo 109 + 7.
"""
class DoublyQueue:
    def __init__(self, size):
        self.size = size
        self.q = [None]*self.size
        self.r, self.f = -1, -1

    def isempty(self):
        if self.f == self.r == -1:
            return True
        else:
            return False

    def isfull(self):
        if (self.r+1)%self.size == self.f:
            return True
        if self.f == -1 and self.r == self.size-1:
            return True
        if self.r == -1 and self.f == 0:
            return True
        return False

    def enqueuerear(self, val):
        if self.isfull():
            return "Full"
        else:
            if self.isempty():
                self.r = (self.r + 1)%self.size
                self.f = self.r
                self.q[self.r] = val
            else:
                self.r = (self.r + 1)%self.size
                self.q[self.r] = val

    def enqueuefront(self, val):
        if self.isfull():
            return "Full"
        else:
            if self.isempty():
                self.f = self.f%self.size
                self.r = self.f
                self.q[self.f] = val
            else:
                self.f = (self.f-1)%self.size
                self.q[self.f] = val
    
    def dequeuerear(self):
        if self.isempty():
            return "Empty"
        else:
            temp = self.q[self.r]
            if self.r == self.f:
                self.r, self.f = -1, -1
            else:
                self.r = (self.r-1)%self.size
            return temp

    def dequeuefront(self):
        if self.isempty():
            return "Empty"
        else:
            temp = self.q[self.f]
            if self.f == self.r:
                self.f, self.r = -1, -1
            else:
                self.f = (self.f+1)%self.size
            return temp

    def front(self):
        if self.isempty():
            return "Empty"
        else:
            return self.q[self.f]

    def rear(self):
        if self.isempty():
            return "Empty"
        else:
            return self.q[self.r]


class Solution:
    def solve(self, A, B):
        ans = 0
        #maxA, minA = [], []
        qmax, qmin = DoublyQueue(len(A)), DoublyQueue(len(A))
        for i in range(B):
            while qmax.isempty() is False and qmax.front() < A[i]:
                qmax.dequeuefront()
            qmax.enqueuefront(A[i])

            while qmin.isempty() is False and qmin.front() > A[i]:
                qmin.dequeuefront()
            qmin.enqueuefront(A[i])

        #maxA.append(qmax.rear())
        #minA.append(qmin.rear())
        ans = (ans + qmax.rear() + qmin.rear())%1000000007

        for i in range(B, len(A)):
            while qmax.isempty() is False and qmax.front() < A[i]:
                qmax.dequeuefront()
            qmax.enqueuefront(A[i])

            if A[i-B] == qmax.rear():
                qmax.dequeuerear()
            #maxA.append(qmax.rear())

            while qmin.isempty() is False and qmin.front() > A[i]:
                qmin.dequeuefront()
            qmin.enqueuefront(A[i])

            if A[i-B] == qmin.rear():
                qmin.dequeuerear()
            #minA.append(qmin.rear())
            ans = (ans + qmax.rear() + qmin.rear())%1000000007
        return ans
        

a = Solution()
A = [5, -1, -1, 2, 2, 5, 2]
print(a.solve(A, 2))    
