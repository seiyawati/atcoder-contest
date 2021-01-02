N = int(input())
S = set(input() for i in range(N))
for s in S:
    if '!' + s in S:
        print(s)
        exit()
print('satisfiable')

# n = int(input())
# arr = []
# for _ in range(n):
#     s = input()
#     arr.append(s)
# for i, S in enumerate(arr):
#     for j in range(n):
#         if i==j:
#             continue
#         else:
#             if S == '!'+arr[j]:
#                 print(arr[j])
#                 exit()
#             elif S == arr[j].lstrip():
#                 print(S)
#                 exit()    
# print('satisfiable')

