def factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
def nthPrime(p):
    n = 0
    for i in range(2,p+1):
        if (factorize(i)[0] == i):
            n += 1
    return n
def parenthify(n):
    if (n == 1):
        return ""
    c = ""
    list = factorize(n)
    for f in list:
        f = "(" + parenthify(nthPrime(f)) + ")"
        c += f
    return c
while (0 == 0):
    n = int(input("What number would you like to parenthify?: "))
    print(parenthify(n))
