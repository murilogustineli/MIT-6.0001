"""
MIT 6.0001 - Introduction to Computation and Programming in Python

Problem Set 0
"""
import numpy as np


def logNumbers(x, y):
    x, y = 2, 3
    print(x ** y)
    print(np.log2(x))


def main():
    x, y = 2, 3
    return logNumbers(x, y)


if __name__ == '__main__':
    main()
    