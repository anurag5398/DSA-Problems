"""
Given a number A, return number of ways you can draw A chords in a circle with 2 x A points such that no 2 chords intersect.
Two ways are different if there exists a chord which is present in one way and not in other.
Return the answer modulo 109 + 7.
"""
#if we select any point for chord, the points are divided into two parts
#these two parts will have separate chords without intersecting
#any point can't select odd point, since if points are divided odd, odd
#then A chords will not be possible without intersection

class Solution:
    #@param A : int -> no of chords
    #@return int -> ways to create A chords
    def chordCnt(self, A):
        dp = [0] * (2*A + 1)
        dp[0], dp[2] = 1, 1

        for i in range(4, 2*A + 1, 2):
            for j in range(0, i-1, 2):
                dp[i]+= dp[j] * dp[i-j-2]

        return dp[2*A]

t = Solution()
print(t.chordCnt(4))

        
