"""
Given a string A denoting a stream of lowercase alphabets.
You have to make new string B. B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. 
if no non-repeating character is found then append '#' at the end of B.
"""

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*self.size
        self.r, self.f = -1, -1

    def enqueue(self, val):
        if (self.f == self.r != -1) or (self.f == -1 and self.r == self.size-1):
            return "Full Queue"
        else:
            self.r = (self.r + 1)%self.size
            self.queue[self.r] = val
    
    def dequeue(self):
        if self.r == self.f == -1:
            return "Empty"
        else:
            self.f = (self.f + 1)%self.size
            temp = self.queue[self.f]
            if self.f == self.r:
                self.f, self.r = -1, -1
            return temp
    
    def front(self):
        if self.f == self.r == -1:
            return "No front"
        else:
            return self.queue[(self.f+1)%self.size]
    
    def notempty(self):
        if self.r == self.f == -1:
            return False
        else:
            return True


class Solution:
    def adddict(self, val, tempdict):
        if val in tempdict:
            tempdict[val]+=1
        else:
            tempdict[val] = 1

    def solve(self, A):
        B = ""
        freqdict = {}
        queue = Queue(len(A))
        for i in range(len(A)):
            queue.enqueue(A[i])
            self.adddict(A[i], freqdict)

            while queue.notempty() and freqdict[queue.front()] > 1:
                queue.dequeue()
            if not queue.notempty():
                B+= "#"
            else:
                B+= queue.front()
        return B

a = Solution()
a.solve("abcabc")

            
            
