# Author: Aleksander Robnik
# Project Euler: Problem 4 - Largest palindrome product
import math


def isPalindrome(num):
    n = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = math.floor(num / 10)
    if n == rev:
        return True
    return False


def LPP():
    lPalindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            testNum = i * j
            if isPalindrome(testNum):
                if (testNum > lPalindrome):
                    lPalindrome = testNum
    return lPalindrome


def main():
    print(LPP())


if __name__ == "__main__":
    main()
