"""
You are given a matrix A which represent operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it.
Operations are of two types:
1 x: push an integer x onto the stack and return -1
2 0: remove and return the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.
A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed.
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, val):
        self.stack.append(val)
        self.count+=1
    def pop(self):
        if self.count < 0:
            return None
        else:
            self.count-=1
            return self.stack.pop()
    def top(self):
        if self.count < 0:
            return None
        else:
            return self.stack[self.count]
    def printstack(self):
        return self.stack

class Solution:
    def __init__(self):
        self.numberdict = dict()
        self.freqdict = dict()
        self.maxfrequency = 0
    def performpush(self, value):
        if value in self.numberdict:
            self.numberdict[value]+=1
        else:
            self.numberdict[value] = 1

        freq = self.numberdict[value]
        if freq > self.maxfrequency:
            self.maxfrequency = freq
        if freq in self.freqdict:
            self.freqdict[freq].push(value)
        else:
            temp = Stack()
            temp.push(value)
            self.freqdict[freq] = temp
        return -1

    def performpop(self):
        if self.maxfrequency == 0:
            return -1
        
        val = self.freqdict[self.maxfrequency].pop()
        self.numberdict[val]-=1
        if self.freqdict[self.maxfrequency].top() is None:
            self.maxfrequency-=1
        return val



    def solve(self, A):
        ans = []
        for i,j in A:
            if i == 1:
                ans.append(self.performpush(j))
            else:
                ans.append(self.performpop())
        return ans


a = [
    [1,5],
    [2, 0],
    [1, 4],
    [1,5],
    [1,4],
    [1,5],
    [1,11],
    [2, 0],
    [2, 0],
    [2, 0],
    [1,5]

]
test = Solution()
print(test.solve(a))

