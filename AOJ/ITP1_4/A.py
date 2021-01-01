a, b = map(int, input().split())
# 置換フィールドに小数点以下の桁数を指定できる
print(f'{a//b} {a%b} {a/b:.10f}')