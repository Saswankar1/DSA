#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if (n % 2 == 1):  # Check for odd numbers first
        print("Weird")
    elif (2 <= n <= 5):  # Check for even numbers within 2-5
        print("Not Weird")
    elif (6 <= n <= 20):  # Check for even numbers within 6-20
        print("Weird")
    else:  # All remaining cases (even numbers greater than 20)
        print("Not Weird")


# one line answer
print("Weird" if n % 2 == 1 or 6 <= n <= 20 else "Not Weird")
