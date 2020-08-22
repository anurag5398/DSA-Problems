"""
Given an array of integers A .
value of a array = max(array) - min(array).
Calculate and return the sum of values of all possible subarrays of A % 109+7.
"""
class Stack:
    def __init__(self):
        self.stack = []
        self.count = -1
    def push(self, val):
        self.count+=1
        self.stack.append(val)
    def pop(self):
        if self.count > -1:
            self.count-=1
            return self.stack.pop()
        else:
            return None
    def top(self):
        if self.count > -1:
            return self.stack[self.count]
        else:
            return None

class Solution:
    def solve(self, A):
        llstack = Stack()
        lstack = Stack()
        rlstack = Stack()
        rsstack = Stack()

        size = len(A)

        leftlargest = [None]*size#leftsmaller
        realleftlargest = [None]*size
        realrightlargest = [None]*size
        rightsmallest = [None]*size


        for i in range(size):
            while llstack.count > -1 and A[llstack.top()] >= A[i]:
                llstack.pop()
            if llstack.count == -1:
                leftlargest[i] = -1
                llstack.push(i)
            if A[llstack.top()] < A[i]:
                leftlargest[i] = llstack.top()
                llstack.push(i)

            while lstack.count > -1 and A[lstack.top()] <= A[i]:
                lstack.pop()
            if lstack.count == -1:
                realleftlargest[i] = -1
                lstack.push(i)
            if A[lstack.top()] > A[i]:
                realleftlargest[i] = lstack.top()
                lstack.push(i)

            j = size-i-1
            
            while rlstack.count > -1 and A[rlstack.top()] < A[j]:
                rlstack.pop()
            if rlstack.count == -1:
                realrightlargest[j] = size
                rlstack.push(j)
            elif A[rlstack.top()] >= A[j]:
                realrightlargest[j] = rlstack.top()
                rlstack.push(j)

            while rsstack.count > -1 and A[rsstack.top()] > A[j]:
                rsstack.pop()
            if rsstack.count == -1:
                rightsmallest[j] = size
                rsstack.push(j)
            elif A[rsstack.top()] <= A[j]:
                rightsmallest[j] = rsstack.top()
                rsstack.push(j)
            
        #print("left smallest ",leftlargest)
        #print("left largest ",realleftlargest)
        #print("right largest ",realrightlargest)
        #print("right smallest ",rightsmallest)
        ans = 0
        for i in range(size):
            maxi = (realrightlargest[i]-i)*(i-realleftlargest[i])
            mini = (rightsmallest[i]-i)*(i-leftlargest[i])
            ans = (ans + A[i]*(maxi-mini))%1000000007
            
        return ans%1000000007


A = [100, 5, 5, -1, -1, 53]
test = Solution()
print(test.solve(A))
