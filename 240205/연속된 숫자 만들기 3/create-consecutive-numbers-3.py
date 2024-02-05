arr = list(map(int, input().split()))
arr.sort()

if arr[2] - arr[1] == arr[1] - arr[0] == 1:
    print(0)
elif arr[2] - arr[1] == 1 or arr[1] - arr[0] == 1:
    print(arr[2]-arr[0]-2)
else:
    print(arr[2]-arr[0]-3)