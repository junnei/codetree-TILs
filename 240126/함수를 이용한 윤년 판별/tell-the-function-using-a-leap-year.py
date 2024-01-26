def is_leap_year2(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            return False
        return True
    return False


def is_leap_year(n):
    if n % 400 == 0:
        return True

    if n % 4 == 0 and n % 100 != 0:
        return True

    return False

n = int(input())
print(str(is_leap_year(n)).lower())