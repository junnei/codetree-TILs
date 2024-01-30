num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int, input().split())
day_to_find = day_of_week.index(input())

days_elapsed = sum(num_of_days[m1:m2])+(d2-d1)
is_day_passed = 1 if day_to_find <= days_elapsed%7 else 0
print(days_elapsed//7 + is_day_passed)