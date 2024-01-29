class Person:
    def __init__(self, name, code, region):
        self.name = name
        self.code = code
        self.region = region

n = int(input())
people = [Person(*input().split()) for _ in range(n)]

people.sort(lambda x: x.name, reverse = True)

print("name", people[0].name)
print("addr", people[0].code)
print("city", people[0].region)