def print_ascend(n):
    if n == 0:
        return
    print_ascend(n - 1)
    print("*"*n)

n = int(input())
print_ascend(n)