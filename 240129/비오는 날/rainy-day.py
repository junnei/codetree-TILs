class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
datas = []

for _ in range(n):
    date, day, weather = input().split()
    if weather == "Rain":
        datas.append(Data(date, day, weather))

datas.sort(lambda x: x.date)

print(f"{datas[0].date} {datas[0].day} {datas[0].weather}")