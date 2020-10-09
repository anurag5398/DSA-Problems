"""
Given a string array A containing N strings representing a dictionary.
You were typing a random word from the dictionary but your keyboard was very old and it might be possible that the key you pressed down got stucked for some time and at the end you got a different string from the original one you were typing.
Like for example suppose you were typing "cat" and it got typed as "ccaaaatttt.
Your are given a string B find out whether this string can be typed by picking any word from the given dictionary A. If it can be typed then return 1 else return 0.
"""
#convert each word to unique char frequency
#Ex: bbiird -> (b, 2),(i, 2),(r, 1),(d, 1)
#Compare with all the words
#To further reduce complexity from n to logn, tries can we used after converting all words

class Solution:
    def convertword(self, word):
        new_word = list()
        char, freq = word[0], 0
        for i in word:
            if i == char: freq+=1
            else:
                new_word.append((char, freq))
                char, freq = i, 1
        new_word.append((char, freq))
        return new_word

    def match_word(self, dictword, inputword):
        n, m = len(dictword), len(inputword)
        if n != m: return False
        for i in range(n):
            if dictword[i][0] != inputword[i][0] or inputword[i][1] < dictword[i][1]:
                return False
        return True

    def solve(self, A: list, B: str) -> int:
        B = self.convertword(B)
        for i, v in enumerate(A):
            A[i] = self.convertword(v)
        for word in A:
            if self.match_word(word, B): return 1
        return 0
        







A = ["hello", "cat", "world", "dog", "bird", "grass", "green", "help", "greet", "great"]
B = "gggraasssa"
t = Solution()
print(t.solve(A, B))