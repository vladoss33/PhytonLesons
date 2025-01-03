class House:

    def __init__(self, name, floor):
        self.name = name
        self.count_floors = floor

    def go_to(self, new_floor):
        if new_floor > self.count_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.count_floors

    def __str__(self):
        return str(f'Название: {self.name}, кол-во этажей: {self.count_floors}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# h1.go_to(5)
# h2.go_to(10)

print(h1)
print(h2)
print(len(h1))
print(len(h2))