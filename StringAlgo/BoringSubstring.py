"""
Given a string A of lowercase English alphabets. Rearrange the characters of the given string A such that there is no boring substring in A.
A boring substring has the following properties:
Its length is 2.
Both the characters are consecutive, for example - "ab", "cd", "dc", "zy" etc.(If the first character is C then the next character can be either (C+1) or (C-1)).
Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.
"""
class Solution:
    def solve(self, A):
        odd, even = [], []
        maxeven, mineven = -1, 26
        maxodd, minodd = -1, 26
        for i in A:
            temp = ord(i)-97
            if temp%2==0:
                even.append(i)
                maxeven = max(temp, maxeven)
                mineven = min(temp, mineven)
            else:
                odd.append(i)
                maxodd = max(temp, maxodd)
                minodd = min(temp, minodd)
        #print(even, chr(mineven+97), chr(maxeven+97))
        #print(odd, chr(minodd+97), chr(maxodd+97))

        if len(even) == 0 or len(odd) == 0:
            return 1
        
        if abs(mineven-maxodd) > 1:
            return 1
        elif abs(minodd-maxeven) > 1:
            return 1
        else:
            return 0

a = Solution()
print(a.solve("acegibh"))