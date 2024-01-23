"""
QUESTION:
  Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


# with built in functions
def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    # we can find the minimum and maximum elements directly using built-in functions
    max_number = max(arr)
    min_number = min(arr)
    # Calculate the minimum sum by excluding the maximum element:
    min_sum = sum(arr) - max_number
    # Calculate the maximum sum by excluding the minimum element:
    max_sum = sum(arr) - min_number
    print(min_sum, max_sum)


# without the built in function
def miniMaxSum_1(arr):
    min_sum = 0
    max_sum = 0
    # Assuming the first element is both minimum and maximum initially
    min_number = arr[0]
    max_number = arr[0]
    for number in arr:
        # Update minimum and maximum numbers based on comparisons
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number
    # Calculate the sums by directly iterating and excluding the found minimum and maximum
    for number in arr:
        if number != min_number:
            min_sum += number
        if number != max_number:
            max_sum += number
    print(max_sum, min_sum)  # Print the maximum sum followed by the minimum sum

        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    minMaxSum_1(arr)
