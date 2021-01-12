# 計算量O(n)
A, B, C, X, Y = map(int, input().split())
s = 10**10
# X, Y<=10**5より10万個以下
# ABをi個買うとすると合計金額は2*C*i+max(X-i, 0)*A+max(Y-i, 0)*B
for i in range(10**5+1):
    s = min(s, 2*C*i+max(X-i, 0)*A+max(Y-i, 0)*B)
print(s)


# 計算量O(1)
A,B,C,X,Y = map(int,input().split())
min_xy = min(X,Y)
max_xy = max(X,Y)
ans1 = 2 * C * min_xy + A * (X-min_xy) + B * (Y-min_xy) # 無駄にならない範囲でABピザを買い、残りを買う
ans2 = A*X + B*Y # ABピザを買わない
ans3 = 2 * C * max_xy # ABピザだけを買う
print (min(ans1,ans2,ans3))