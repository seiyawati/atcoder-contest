import sys
import itertools

times = sys.argv
times.pop(0)
length = len(times)

time_list = []

def list_difference(l1, l2):
    result = l1.copy()
    for value in l2:
        if value in result:
            result.remove(value)

    return result

for t in itertools.combinations(times, length//2):
    l1 = list(t)
    l2 = list_difference(times, l1)
    l1 = list(map(int, l1))
    l2 = list(map(int, l2))
    max_time = max(sum(l1), sum(l2))
    time_list.append(max_time)

print(min(time_list))
