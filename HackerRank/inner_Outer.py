# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B), numpy.outer(A, B), sep='\n')
