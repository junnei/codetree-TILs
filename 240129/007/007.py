class Meeting:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

a, b, c = input().split()

a = Meeting(a, b, c)

print(f"secret code : {a.code}")
print(f"meeting point : {a.point}")
print(f"time : {a.time}")