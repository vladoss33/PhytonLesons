class House:

    def __init__(self, name, floor):
        self.name = name
        self.count_floors = floor

    def go_to(self, new_floor):
        if new_floor>self.count_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.count_floors

    def __str__(self):
        return str(f'Название: {self.name}, кол-во этажей: {self.count_floors}')

    def __eq__(self, other):    # ==
        return self.name == other.name and self.count_floors == other.count_floors

    def __lt__(self, other):    # <
        return self.count_floors < other.count_floors

    def __le__(self, other):    # <=
        return self.count_floors <= other.count_floors

    def __gt__(self, other):    # >
        return self.count_floors > other.count_floors

    def __ge__(self, other):    # >=
        return self.count_floors >= other.count_floors

    def __ne__(self, other):    # !=
        return self.count_floors != other.count_floors

    def __add__(self, other):
        if isinstance(other, int):
            self.count_floors += other
            return self
        elif isinstance(other, House):
            self.count_floors += other.count_floors
            return self

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __radd__(self, other):
        self.__add__(other)
        return self
#_________________________________________________________________


h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)



print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
