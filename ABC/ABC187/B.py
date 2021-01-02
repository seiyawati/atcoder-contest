n = int(input())
x = []
y = []
for i in range(n):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)

count = 0
for i in range(n):
    for j in range(i):
        # absは絶対値を求める関数
        if abs((y[j]-y[i])/(x[j]-x[i])) <= 1:
            count += 1
print(count)


# i_x = 0
# i_y = 0
# j_x = 0
# j_y = 0
# count = 0
# n = int(input())
# for k in range(n):
#     x, y = map(int, input().split())
#     if k == 0:
#         i_x = x
#         i_y = y
#     else:
#         j_x = x
#         j_y = y
#         if (i_y-j_y)/(i_x-j_x) <= 1 and (i_y-j_y)/(i_x-j_x) >= -1:
#             count += 1
#     i_x = j_x
#     i_y = j_y
# print(count)




        

    