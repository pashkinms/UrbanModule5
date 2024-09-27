class House:
    def __init__(self, name: str, amount_floors: int):
        self.name = name
        self.amount_floors = amount_floors

    def go_to(self, new_floor: int):
        if new_floor in range(1, self.amount_floors + 1):
            for i in range(1, new_floor +1):
                print(i)
        else:
            print("Such floor does not exist!")

    def __len__(self):
        return self.amount_floors
    def __str__(self):
        return f'Name: {self.name}, number of floors: {self.__len__()}'

    def __eq__(self, other):
        return self.amount_floors == other.amount_floors

    def __lt__(self, other):
        return self.amount_floors < other.amount_floors

    def __le__(self, other):
        return self.amount_floors <= other.amount_floors

    def __gt__(self, other):
        return self.amount_floors > other.amount_floors

    def __ge__(self, other):
        return self.amount_floors >= other.amount_floors

    def __ne__(self, other):
        return self.amount_floors != other.amount_floors

    def __add__(self, value):
        self.amount_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


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