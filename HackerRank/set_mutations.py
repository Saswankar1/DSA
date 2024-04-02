a = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    operation, _ = input().split()
    new_elements = set(map(int, input().split())) 

    perform = f'A.{operation}({new_elements})'
    eval(perform)

print(sum(A))
