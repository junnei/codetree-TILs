class Data:
    def __init__(self, x, y, z):
        self.x = x
        self.y = int(y)
        self.z = float(z)

n = 5
datas = []
for i in range(n):
    x, y, z = input().split()
    datas.append(Data(x, y, z))

print("name")
datas.sort(lambda x : x.x)

for data in datas:
    print(data.x, data.y, data.z)
print()
print("height")
datas.sort(lambda x : -x.y)

for data in datas:
    print(data.x, data.y, data.z)