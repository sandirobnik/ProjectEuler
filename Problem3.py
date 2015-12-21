# Author: Aleksander Robnik
# Project Euler: Problem 3 - Largest prime factor

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
    return True


def LPF(n):
    gEnd = False
    lEnd = False
    dev = 2
    lFactor = 0

    while not gEnd:
        while not lEnd:
            if n % dev == 0:
                n /= dev
                dev = 2
                lEnd = True
                if dev > lFactor:
                    lFactor = dev
            dev += 1
        if (isPrime(n)):
            if n > lFactor:
                lFactor = n
            gEnd = True
        else:
            lEnd = False
    return lFactor


def main():
    print(LPF(600851475143))


if __name__ == "__main__":
    main()
