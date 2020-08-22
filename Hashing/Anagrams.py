"""
Given an array A of N strings, return all groups of strings that are anagrams.
Represent a group by a list of integers representing the index(1-based) in the original list. Look at the sample case for clarification.
NOTE: Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'.
"""
class Solution:
    def calculatehash(self, string):
        char = [0]*26
        for i in string:
            char[ord(i)-97]+=1
        return hash(tuple(char))

    def adddict(self, val, index, tempdict):
        if val in tempdict:
            tempdict[val].append(index+1)
        else:
            tempdict[val] = [index+1]

    def anagrams(self, A):
        hashdict = dict()
        for i, string in enumerate(A):
            val = self.calculatehash(string)
            self.adddict(val, i, hashdict)
            print("i {} ,string {}, hashdict {}".format(i, string, hashdict))
        
        return list(hashdict.values())

a = Solution()
print(a.solve(["rat", "tar", 'art']))