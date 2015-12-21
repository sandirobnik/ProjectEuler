# Author: Aleksander Robnik
# Project Euler: Problem 9 - Special Pythagorean triplet
import math


def SPT(n):
    tripledProd = 0

    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if math.pow(i, 2) + math.pow(j, 2) == math.pow(k, 2):
                    if i + j + k == n:
                        print(i, j, k)
                        tripledProd = i * j * k
    return tripledProd


def main():
    print(SPT(1000))


if __name__ == "__main__":
    main()
