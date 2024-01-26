def calculate(a, b, o):
    if o == '+':
        return a+b
    elif o == '-':
        return a-b
    elif o == '/':
        return a//b
    elif o == '*':
        return a*b

a, o, c = input().split()

if o in ['+', '-', '/', '*']:
    print(a, o, c, '=', calculate(int(a), int(c), o))
else:
    print("False")