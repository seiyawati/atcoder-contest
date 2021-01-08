# 標準偏差
import math
while True:
	n=int(input())
	if n==0:break
	l=list(map(int, input().split()))
	sum=0
	for i in l:sum+=i
    # /はint同士でも結果はfloat
	a=float(sum)/n
    # 0.0
	sum2=.0
    # float
	for i in l:sum2+=(i-a)**2
	print(math.sqrt(sum2/n))