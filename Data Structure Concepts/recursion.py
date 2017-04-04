#!/usr/bin/python3.4
# Gentoo's python interpreter
# Author: Lu
# Purpose: Recursion in python3.4


def factorial(n):
    if n == 1:
        print("factorial has been called with n = " + str(n))
        return 1
    else:
        res = n * factorial(n - 1)
        print("intermediate result for ", n,
              " * factorial(", n - 1, "): ", res)
        return res


print(factorial(5))
print("-----------------")

print("Fibbonachi Sequence")
