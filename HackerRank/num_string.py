
"""
QUESTION:
  Read an integer, , from STDIN. Without using any string methods, try to print the following:
    1. Note that "" represents the consecutive values in between.
  
    2. Example
        Input Format: 3
        Output Format: 123
  
  Print the list of integers from  through  as a string, without spaces.
"""

## Answer:
if __name__ == '__main__':
    n = int(input())
    test_string = ""
    for i in range(n):
        test_string += f"{i+1}"
    print(test_string)
