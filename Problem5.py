# Author: Aleksander Robnik
# Project Euler: Problem 5 - Smallest multiple

def smallestMultiple():
    isFound = False
    lFound = False
    i = 1
    n = 0

    while not isFound:
        n += 20
        while not lFound:
            if n % i != 0:
                lFound = True
            if i > 20:
                lFound = True
                isFound = True
            i += 1
        lFound = False
        i = 1
    return n


def main():
    print(smallestMultiple())


if __name__ == "__main__":
    main()
