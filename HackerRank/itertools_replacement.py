from itertools import combinations_with_replacement as c
S, k = input().split()

for data in c(sorted(S), int(k)):
    print(''.join(data))