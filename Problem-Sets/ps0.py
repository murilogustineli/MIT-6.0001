"""
MIT 6.0001 - Introduction to Computation and Programming in Python

Problem Set 0
"""
import numpy as np


def computeNumbers(x, y):
    x, y = 2, 3
    print(x ** y)
    print(np.log2(x))


def main():
    x, y = 2, 3
    return computeNumbers(x, y)


if __name__ == '__main__':
    main()
