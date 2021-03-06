import math
weight, tall, f_bmi = map(int, input().split())
c_bmi = 10000 * weight / tall/ tall
if c_bmi > f_bmi:
    n_weight = f_bmi / 10000 * tall * tall
    print(math.ceil(weight-n_weight))
else:
    print(0)

