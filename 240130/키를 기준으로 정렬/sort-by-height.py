class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)

n = int(input())
people = [Person(*input().split()) for _ in range(n)]
people.sort(lambda x : x.height)
for person in people:
    print(person.name, person.height, person.weight)