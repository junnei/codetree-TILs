n = int(input())
arr = [
    [0] + list(map(int, input().split()))
    for _ in range(2)
]

sum_val = 0
for idx, people in enumerate(arr[0]):
    sum_val += idx*people
    
last_val = 0
for idx, people in enumerate(arr[1]):
    last_val += idx*people

print(last_val - sum_val)