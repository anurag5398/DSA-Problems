#Given a array A of non negative integers, arrange them such that they form the largest number.

'''
Create a comparator function that can be passed as key to sort method.
logic : str(x)+str(y) > str(y)+str(x)
'''

def comparator(x, y):
    x, y = str(x), str(y)
    return (int(x+y) > int(y+x)) - (int(x+y) < int(y+x))

#all the function not req. (main: lt, gt, eq)
def newsort(mycomp):
    class temp:
        def __init__(self, number, *args):
            self.number = number
        def __lt__(self, other):
            return mycomp(self.number, other.number) < 0
        def __gt__(self, other):
            return mycomp(self.number, other.number) > 0
        def __eq__(self, other):
            return mycomp(self.number, other.number) == 0
        def __le__(self, other):
            return mycomp(self.number, other.number) <= 0
        def __ge__(self, other):
            return mycomp(self.number, other.number) >= 0
        def __ne__(self, other):
            return mycomp(self.number, other.number) != 0
    return temp

A = [54, 546, 548, 60]

print(sorted(A, key=newsort(comparator), reverse=True))