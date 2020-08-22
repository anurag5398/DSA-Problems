#cyclic Q using array
class CyclicQueue:
    def __init__(self):
        self.size = 5
        self.queue = [None]*self.size
        self.f, self.r = -1, -1
    def enqueue(self, val):
        if (self.r == self.f != -1) or (self.f == -1 and self.r == self.size-1):
            print("Full")
            return
        else:
            self.r = (self.r + 1)%self.size
            self.queue[self.r] = val
            print("added ",val)
    def dequeue(self):
        if self.r == self.f == -1:
            print("Empty")
            return
        else:
            self.f = (self.f + 1)%self.size
            if self.f == self.r:
                self.f, self.r = -1, -1
    def front(self):
        if self.r == self.f == -1:
            print("Empty front")
        else:
            return self.queue[(self.f + 1)%self.size]


