n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

nums = [-1] * 11
cnt = 0
for i, direction in arr:
    if nums[i] == -1:
        nums[i] = direction
    else:
        if nums[i] != direction:
            cnt += 1
            nums[i] = direction
print(cnt)