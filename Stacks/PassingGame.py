"""
There is a football event going on in your city. In this event, you are given A passes and players having ids between 1 and 106.
Initially some player with a given id had the ball in his possession. You have to make a program to display the id of the player who possessed the ball after exactly A passes.
There are two kinds of passes:
1) ID
2) 0
For the first kind of pass, the player in possession of the ball passes the ball "forward" to player with id = ID.
For the second kind of a pass, the player in possession of the ball passes the ball back to the player who had forwarded the ball to him.
In the second kind of pass "0" just means Back Pass.
Return the ID of the player who currently posseses the ball.
"""
#A- length of C B-initial element   C-array

class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, value):
        self.stack.append(value)
        self.count+=1
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.count-=1
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return -1
    def printstack(self):
        print(self.stack)

    def isempty(self):
        if self.count == -1:
            return 1
        return 0

class Solution:
    def solve(self, A, B, C):
        passes = Stack()
        passes.push(B)
        for i in C:
            if i == 0:
                passes.pop()
            else:
                passes.push(i)
        return passes.top()

temp = Solution()
print(temp.solve(10, 23, [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]))