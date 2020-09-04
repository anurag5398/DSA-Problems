"""
Two people are playing the Coin Game! The rules of the game are:
The game is played on a line of N squares. The i-th square contains A[i] coins.
The players move in alternate turns. During each move, the current player must remove exactly 1 coin from i-th square and move it to j-th square if and only if 1 <= j < i.
The game ends when all coins are in square 1 and nobody can make a move. The first player to have no available move loses the game.
Determine whether the person who wins the game is the first or second person to move. Assume both players move optimally.
"""

#basically if mirror move is available player 2 wins
#so for all even piles mirror moves are available
#for odd piles except the last coin all other can be mirrored
#for last coin assume location i, it has i moves from (0 to i-1)
#problem is reduced to normal nim game

#in nim game if even bit is set for all position, i.e all position could be countered 
#then player 2 wins

class Solution:
    #@param A : list of int
    #@return string
    def solve(self, A):
        xorSum = 0
        for i, score in enumerate(A):
            if score % 2 != 0:
                xorSum^= i
        #print(xorSum)
        return "First" if xorSum else "Second"


A = [0, 2, 0, 0, 0]
t = Solution()
print(t.solve(A))


