# Author: Aleksander Robnik
# Project Euler: Problem 7 - 10001st prime

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


def primeNumbers(pos):
    ifFound = False
    count = 0
    n = 0

    while not ifFound:
        n += 1
        if isPrime(n):
            count += 1
        if count == pos:
            ifFound = True
    return n


def main():
    print(primeNumbers(10001))


if __name__ == "__main__":
    main()
