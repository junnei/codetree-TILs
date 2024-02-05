n = int(input())
arr = list(map(int, input().split()))

arr.sort()

pos = -1
neg = -1

negative = True
for i, num in enumerate(arr):
    if num >= 0 and negative:
        negative = False
        neg = i - 1
    if num > 0:
        pos = i
        break
        
zero = pos - neg -1
# neg : 음수 마지막 index
# neg + 1 : 음수 개수
# pos : 양수 처음 index
# n - pos: 양수 개수
# zero : pos - neg - 1 개 있음

len_pos = n - pos
len_neg = neg + 1
zero = pos - neg -1
if len_pos >= 3:
    print(max(arr[-1]*arr[-2]*arr[-3], arr[0]*arr[1]*arr[-1]))
elif len_pos >= 1 and len_neg >= 2:
    print(arr[0]*arr[1]*arr[-1])
elif zero >= 1:
    print(0)
else:
    nums = []
    i, j = 0, 0
    while i+j < 3:
        if arr[neg-i]*(-1) <= arr[pos+j]:
            nums.append(arr[neg-i])
            i += 1
        else:
            nums.append(arr[pos+j])
            j += 1
    print(nums[0]*nums[1]*nums[2])