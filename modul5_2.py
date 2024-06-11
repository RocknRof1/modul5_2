class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNuwNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Новый номер этажа', self.numberOfFloors)

my_house = House()
my_house.setNuwNumberOfFloors(7)

