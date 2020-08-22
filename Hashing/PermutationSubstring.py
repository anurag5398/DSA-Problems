"""
You are given two strings A and B of size N and M respectively.
You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.
"""
A = "abc"
B = "abcbac"

#below is a perfect solution. But is throwing MLE for huge inputs.
class Solution:
    def solve(self, A, B):
        alphabets = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
             'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 
             'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
        pattern = 1
        for i in A:
            pattern*= alphabets[i.lower()]


        running = []
        for i in B:
            running.append(alphabets[i.lower()])
        temp = 1
        for i, val in enumerate(running):
            temp*= val
            running[i] = temp
        running.insert(0, 1)
        #print(running)



        i, j = 0, len(A)
        ans = 0
        while j <= len(B):
            val = running[j]//running[i]
            if val == pattern:
                #print(val, B[i:j])
                ans+=1
            i+=1
            j+=1
        return ans
        
test = Solution()
#print(test.solve(A, B))

class HashCheck:
    def solve(self, A, B):
        pattern = [0]*26
        string = [0]*26
        for i in A:
            pos = ord(i)-97
            pattern[pos]+=1
        
        for j in range(len(A)):
            pos = ord(B[j])-97
            string[pos]+=1
        j+=1
        count = 0
        if hash(tuple(string)) == hash(tuple(pattern)):
            count+=1
        
        for i in range(len(B)-len(A)):
            string[ord(B[i])-97]-=1
            string[ord(B[j])-97]+=1

            if hash(tuple(string)) == hash(tuple(pattern)):
                count+=1
            j+=1
        print(count)

test2 = HashCheck()
test2.solve(A, B)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

