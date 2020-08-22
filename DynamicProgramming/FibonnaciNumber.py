"""
Given a positive integer A, write a program to find the Ath Fibonacci number.
In a Fibonacci series, each term is the sum of the previous two terms and the first two terms of the series are 0 and 1. i.e. f(0) = 0 and f(1) = 1. Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.
NOTE: 0th term is 0. 1th term is 1 and so on.
"""
def fib(number):
    if number < 2: return number
    if dp[number] > 0: return dp[number]
    dp[number] = fib(number-1) + fib(number-2)
    return dp[number]

def main():
    A = int(input())
    global dp
    dp = [0]*(A+1)
    dp[1] = 1
    return fib(A)


if __name__ == '__main__':
    print(main())