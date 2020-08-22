class DoublyQueue:
    def __init__(self, val):
        self.size = val
        self.queue = [None]*self.size
        self.r, self.f = -1, -1

    def isfull(self):
        if (self.r + 1)%self.size == self.f:
            return True
        if self.f == -1 and self.r == self.size-1:
            return True
        if self.f == 0 and self.r == -1:
            return True
        return False

    def isempty(self):
        if self.f == self.r == -1:
            return True
        else:
            return False

    def enqueuerear(self, val):
        if not self.isfull():
            self.r = (self.r + 1)%self.size
            self.queue[self.r] = val
            #print("Enqueued REar")
        else:
            print("Full")
    
    def enqueuefront(self, val):
        if not self.isfull():
            if self.f != -1:
                self.f = (self.f - 1)%self.size
            else:
                self.f = self.f%self.size
            self.queue[self.f] = val
            #("Enqueued Front ",self.f)
        else:
            print("Full val {} self.f {} self.r {}".format(val, self.f, self.r))

    def dequeuerear(self):
        if not self.isempty():
            if self.r == -1:
                self.r = (self.r)%self.size
            
            temp = self.queue[self.r]
            if self.r == self.f:
                self.f, self.r = -1, -1
            else:
                self.r = (self.r - 1)%self.size
            if self.f == -1 and self.r == self.size-1:
                self.r, self.f = -1, -1
            return temp
        else:
            print("Empty")

    def dequeuefront(self):
        if not self.isempty():
            if self.f == -1:
                self.f = (self.f + 1)%self.size

            temp = self.queue[self.f]
            if self.f == self.r:
                self.f, self.r = -1, -1
            else:
                self.f = (self.f + 1)%self.size
            if self.f == 0 and self.r == -1:
                self.r, self.f = -1, -1
            return temp
        else:
            print("Empty")

    def front(self):
        if self.isempty():
            print("No front")
        else:
            if self.f == -1:
                return self.queue[0]
            else:
                return self.queue[self.f]

    def rear(self):
        if self.isempty():
            print("No rear")
        else:
            if self.r == -1:
                return self.queue[self.size-1]
            else:
                return self.queue[self.r]

class Solution:
    def slidingMaximum(self, A, B):
        q = DoublyQueue(20)
        ans = []

        for i in range(B):
            while q.isempty()==False and q.front() < A[i]:
                q.dequeuefront()
            q.enqueuefront(A[i])
        ans.append(q.rear())
        
        for i in range(B, len(A)):
            while q.isempty()==False and q.front() < A[i]:
                q.dequeuefront()
            q.enqueuefront(A[i])
            if A[i-B] == q.rear():
                q.dequeuerear()
            

            ans.append(q.rear())

        return ans

A = [1,3,5,7,6,4,0,5]
a = Solution()
print(a.slidingMaximum(A, 3))