def is_magic_number(num):
    if num%2 == 0 and sum([int(i) for i in str(num)]) % 5 == 0:
        return "Yes"
    else:
        return "No"

n = int(input())
print(is_magic_number(n))