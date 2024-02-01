# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m=map(int,input().split())

print(str(numpy.eye(n, m,k=0)).replace('0',' 0').replace('1',' 1'))
                        
