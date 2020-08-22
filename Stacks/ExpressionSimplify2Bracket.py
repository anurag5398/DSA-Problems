"""
Given two strings A and B. Each string represents an expression consisting of lowercase english alphabets, '+', '-', '(' and ')'.
The task is to compare them and check if they are similar. If they are similar return 1 else return 0.
NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’ and every operand appears only once.
"""
class Stack:
    def __init__(self):
        self.stack = ['+']
        self.count = 0
        self.stacksign = '+'
    def push(self, sign):
        self.stack.append(sign)
        self.count+=1
        if self.stacksign == '+' and sign == '-':
            self.stacksign = '-'
        elif self.stacksign == '-' and sign == '-':
            self.stacksign = '+'
    def pop(self):
        if self.count > -1:
            sign = self.stack.pop()
            self.count-=1
            if self.stacksign == '+' and sign == '-':
                self.stacksign = '-'
            elif self.stacksign == '-' and sign == '-':
                self.stacksign = '+'
    def checksign(self):
        if self.count > -1:
            return self.stacksign
        else:
            return '+'



class Solution:
    def calculatesign(self, signs):
        if len(signs) != 3:
            print(signs, "Fault")
        pos, neg = 0, 0
        for i in signs:
            if i == '+':
                pos+=1
            else:
                neg+=1
        pos, neg = pos%2, neg%2
        if neg == 0 and pos == 1:
            return '+'
        elif neg == 1 and pos == 0:
            return '-'
        elif neg == 1 and pos == 1:
            return '-'
        elif neg == 0 and pos == 0:
            return '+'


    def simplify(self, string):
        signstack = Stack()
        i = 0
        ans = set()
        while i < len(string):
            #print("on {}".format(string[i]))
            if string[i] == '(':
                if i == 0 or string[i-1].isalpha() or string[i-1] == '+':
                    signstack.push('+')
                elif string[i-1] == '-':
                    signstack.push('-')
            elif string[i] == '-' or string[i] == '+':
                pass
            elif string[i].isalpha():
                temp = "+"
                if i == 0 or string[i-1] == '+' or string[i-1] == '(':
                    temp+= '+'
                elif string[i-1] == '-':
                    temp+= '-'
                
                temp+= signstack.checksign()
                #print(temp)
                sign = self.calculatesign(temp)
                ans.add(sign+string[i])
            elif string[i] == ')':
                signstack.pop()
            i+=1
        return ans
    
    def solve(self, A, B):
        word1 = self.simplify(A)
        word2 = self.simplify(B)
        print(word1)
        print(word2)
        if word1 == word2:
            return 1
        else:
            return 0

word = "-(a+b-(c-d))"
word2 =  "-a-b+c-d"
test = Solution()
print(test.solve(word, word2))
