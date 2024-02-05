n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

num = sum(arr)//n

sum_val = 0
for i in arr:
    sum_val += abs(num-i)
print(sum_val//2)