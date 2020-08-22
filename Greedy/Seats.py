"""
There is a row of seats represented by string A. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.
An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.
In one jump a person can move to the adjacent seat (if available).
NOTE: 1. Return your answer modulo 107 + 3.
"""

#all the points should move towards the median

class Solution:
    #paramA : string
    #return integer
    def solve(self, A):
        seats = []
        for i in range(len(A)):
            if A[i] == 'x':
                seats.append(i)

        moves = 0
        i = len(seats)//2
        diff = seats[i]-i
        for seat in seats:
            shift = abs(seat-diff)
            moves = (moves + shift)%(10**7+3)
            diff+=1
        return moves%(10**7+3)

t = Solution()
A = "....xxx"
print(t.solve(A))

        
