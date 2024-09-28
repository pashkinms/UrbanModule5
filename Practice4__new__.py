class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, amount_floors):
        self.name = name
        self.amount_floors = amount_floors

    def __del__(self):
        print(f"{self.name} destroyed, but it's still in history.")

    def go_to(self, new_floor: int):
        if new_floor in range(1, self.amount_floors + 1):
            for i in range(1, new_floor + 1):
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
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)