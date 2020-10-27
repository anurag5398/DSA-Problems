"""
Two players have got a string A, consisting of lowercase English letters. They play a game that is described by the following rules:

The players move in turns; In one move the player can remove an arbitrary letter from string A.
If the player before his turn can reorder the letters in string A so as to get a palindrome, this player wins.
NOTE:

A palindrome is a string that reads the same both ways (from left to right, and vice versa). For example, string "abba" is a palindrome and string "abc" isn't.
"""

#remove mirror items i.e even elements
#now game depends on odd occurance

#virtual corner case: abac -> if p1 removes c p2 wins -> if p1 removes b/c still p2 wins after 2 chance. (so not a corner)

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A: str) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        for i in A:
            count[i]+=1
        
        oddvals = 0
        for v in count.values():
            if v%2 != 0: oddvals+=1
        
        if oddvals % 2 == 0: return 2
        return 1
