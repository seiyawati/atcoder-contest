time = input().split()
abs_times = []
for i in range(6):
    if i == 5:
        abs_times.append(abs(int(time[0]) - int(time[6])))
    abs_times.append(abs(int(time[i + 1]) - int(time[i])))
print(max(abs_times))
