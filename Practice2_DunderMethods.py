
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

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))