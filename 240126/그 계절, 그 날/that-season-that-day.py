def is_valid_date(y, m, d):
    if d <= date_limit(y, m):
        return True
    return False

def is_leap_year(y):
    if y % 400 == 0:
        return True
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False

def get_season(m):
    if m >= 3 and m <= 5:
        return "Spring"
    elif m >= 6 and m <= 8:
        return "Summer"
    elif m >= 9 and m <= 11:
        return "Fall"
    else:
        return "Winter"

def date_limit(y, m):
    if m == 2:
        return 29 if is_leap_year(y) else 28

    if m <= 7:
        if m % 2 == 1:
            return 31
        else:
            return 30
    else:
        if m % 2 == 1:
            return 30
        else:
            return 31

y, m, d = map(int, input().split())

if is_valid_date(y, m, d):
    print(get_season(m))
else:
    print(-1)