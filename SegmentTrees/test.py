
def fastpow(number, power):
    if power == 0: return 1
    temp = fastpow(number, power//2)
    if power %2 == 0:
        return temp*temp
    else:
        return number*temp*temp



print(fastpow(2, 13))

po