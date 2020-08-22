"""
Given an array of integers A of size N.
A triplet (i, j, k), i <= j <= k is called a power triplet if A[i] ^ A[i+1] ^....A[j-1] = A[j] ^.....^A[k].
Where, ^ denotes bitwise xor.
Return the count of all possible power triplets. Since the answer could be large return answer % 109 +7.
"""
#Question was part of tries, but solved it using prefix XOR and dict(hashmap)
#if 2 same same element found in xor prefix then all the between terms will follow the above property.

class Solution:
    #add to xordict
    def adddict(self, key, val, tempdict):
        if key in tempdict:
            tempdict[key].append(val)
        else:
            tempdict[key] = [val]
    
    #calculate number of elements between any two same element  
    def between(self, templist):
        if len(templist) < 2: return 0
        tempans = 0
        for i in range(len(templist)):
            for j in range(i+1, len(templist)):
                tempans = (tempans + (templist[j]-templist[i]-1))%(10**9+7)
        return tempans%(10**9+7)              

    #paramA = Input array        
    def solve(self, A):
        temp = 0
        #maintain a dict 
        xordict = dict()
        xordict[0] = [0]
        #calculate prefix sum and at the same time populate dict
        for i, val in enumerate(A):
            temp^= val
            A[i] = temp
            self.adddict(temp, i+1, xordict)
        A.insert(0, 0)
        ans = 0
        for valList in xordict.values():
            ans = (ans + self.between(valList))%(10**9+7)
        return ans%(10**9+7)
        
# Another Solution
