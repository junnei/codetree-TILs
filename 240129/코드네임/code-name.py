class User:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)

arr = [User(*input().split()) for _ in range(5)]

arr.sort(lambda x : x.score)
print(f"{arr[0].name} {arr[0].score}")