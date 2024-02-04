n = int(input())
arr = input()


for len_str in range(1, n+1):
    found = False
    for i in range(n-len_str+1):
        if arr[i:i+len_str] in arr[:i]+arr[i+len_str:]:
            found = True
            break
    if not found:
        print(len_str)
        break