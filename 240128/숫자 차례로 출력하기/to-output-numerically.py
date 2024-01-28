def print_descend(n):
    if n == 0:
        print()
        return
    print(n, end=" ")
    print_descend(n - 1)

def print_ascend(n):
    if n == 0:
        return
    print_ascend(n - 1)
    print(n, end=" ")

n = int(input())
print_ascend(n)
print()
print_descend(n)