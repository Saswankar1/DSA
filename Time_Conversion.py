"""
  Q. Given a time in -hour AM/PM format, convert it to military (24-hour) time.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    # Extract hour, minutes, and seconds
    hour, minutes, seconds = s[:2], s[3:5], s[6:8]

    # Check AM/PM and adjust hour if necessary
    if s[-2:] == "PM" and hour != "12":
        hour = int(hour) + 12
    elif s[-2:] == "AM" and hour == "12":
        hour = "00"

    # Combine and return the converted time
    return f"{hour}:{minutes}:{seconds}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
