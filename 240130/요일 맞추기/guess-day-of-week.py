num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

m1, d1, m2, d2 = map(int, input().split())
if m1<m2 or (m1==m2 and d1<=d2):
    print(days[((sum(num_of_days[m1:m2])+(d2-d1))+1)%7])
else:
    print(days[(-(sum(num_of_days[m2:m1])+(d1-d2))+1)%7])