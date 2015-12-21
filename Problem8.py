# Author: Aleksander Robnik
# Project Euler: Problem 8 - Largest product in a series


def LPS(number):
    currentProduct = 1
    maxProduct = 1

    for i in range(0, len(number) - 13):
        for j in range(i, i + 13):
            currentProduct *= int(number[j])
        if currentProduct > maxProduct:
            maxProduct = currentProduct
        currentProduct = 1
    return maxProduct


def main():
    with open("1000digit.txt", "rt") as inFile:
        text = inFile.read()
    print(LPS(text))


if __name__ == "__main__":
    main()
