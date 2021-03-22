C = input().split()
A = input().split()
Alice = 0
for i in range(6):
    if A[i] == 'Alice':
        Alice += int(C[i])
print(Alice)