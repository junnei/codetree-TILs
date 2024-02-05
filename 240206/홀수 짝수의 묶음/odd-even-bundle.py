n = int(input())
arr = list(map(lambda x: int(x)%2, input().split()))


even, odd = arr.count(0), arr.count(1)

while True:
    if even < odd:
        odd -= 2
        even += 1
    elif even - odd > 1:
        even -= 1
    else:
        break
print(odd+even)