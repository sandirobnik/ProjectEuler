# Author: Aleksander Robnik
# Project Euler: Problem 1 - Multiples of 3 and 5

def multiples(lowr, highr):
    sum = 0
    for i in range(lowr + 1, highr + 1):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum


def main():
    sum = multiples(3, 999)
    print(sum)


if __name__ == "__main__":
    main()
