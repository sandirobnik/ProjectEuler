# Author: Aleksander Robnik
# Project Euler: Problem 2 - Even Fibonacci numbers

def fubonacci(maxNumber):
    a = 1
    b = 2
    tmp = 0
    sum = 2

    while b < maxNumber:
        tmp = b
        b = b + a
        a = tmp
        if b % 2 == 0:
            sum += b
    return sum


def main():
    sumFibonacci = fubonacci(4000000)
    print(sumFibonacci)


if __name__ == "__main__":
    main()
