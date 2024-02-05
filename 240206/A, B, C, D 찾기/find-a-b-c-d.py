arr = list(map(int, input().split()))

arr.sort()

a = arr[0]
b = arr[1]
cd = arr[-1] - a - b
c = [n for n in arr if n <= a+b]
d = [n for n in arr if n <= cd - c[0]]

def get_num(c, d):
    for i in c:
        for j in d:
            if i <= j and i+j == cd:
                return i, j
c, d = get_num(c, d)
print(a, b, c, d)