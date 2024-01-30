a, b = map(int, input().split())
binary = list(map(int, input()))
num = 0

for i in range(len(binary)):
    num = num * a + binary[i]

n = num

digits = []

while True:
    if n < b:
        digits.append(n)
        break

    digits.append(n % b)
    n //= b

for digit in digits[::-1]:
    print(digit, end="")