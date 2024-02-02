n = int(input())
times = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_running_time = 0
MAX_TIME = 1000
for idx in range(n):
    time_table = [0 for _ in range(MAX_TIME+1)]
    for a, b in (times[:idx]+times[idx+1:]):
        for i in range(a, b):
            time_table[i] = 1
    running_time = sum(time_table)
    max_running_time = max(max_running_time, running_time)

print(max_running_time)