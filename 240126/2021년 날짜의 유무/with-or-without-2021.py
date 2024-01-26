def is_valid_date(a, b):
    if date_limit(a) and b <= date_limit(a):
            return True
    return False

def date_limit(a):
    if a == 2:
        return 28
    if a <= 7:
        if a % 2 == 1:
            return 31
        else:
            return 30
    elif a <= 12:
        if a % 2 == 1:
            return 30
        else:
            return 31
    else:
        return False

a, b = map(int, input().split())

if is_valid_date(a, b):
    print("Yes")
else:
    print("No")