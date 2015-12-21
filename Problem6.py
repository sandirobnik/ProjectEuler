# Author: Aleksander Robnik
# Project Euler: Problem 6 - Sum square difference
import math


def SQD():
    sumOfSquares = 0
    squareOfSums = 0

    for i in range(1, 101):
        sumOfSquares += math.pow(i, 2)
        squareOfSums += i
    squareOfSums = math.pow(squareOfSums, 2)
    return squareOfSums - sumOfSquares


def main():
    print(SQD())


if __name__ == "__main__":
    main()
