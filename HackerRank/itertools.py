# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
word , length  = input().split()
for i in range(1, int(length)+1):
    for j in combinations(sorted(word), i):
        print (''.join(j))