def print_string(n):
    if n == 0:
        return
    print_string(n - 1)
    print("HelloWorld")

n = int(input())
print_string(n)