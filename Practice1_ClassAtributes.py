
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



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)