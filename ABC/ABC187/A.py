A, B = map(str, input().split())
S_A = 0
S_B = 0
for a in A:
    S_A += int(a)
for b in B:
    S_B += int(b) 
print(max(S_A, S_B))

