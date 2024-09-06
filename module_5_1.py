# Домашняя работа по уроку "Атрибуты и методы объекта."
# Дополнил код вводом произвольных исходных данных
gk = input('введите имя дома: ')
maxfloor = input('введжите количество этажей дома: ')
floor = input('введите номер необходимого этажа: ')
# Объявление класса House
class House():
    # инициализация характеристик класса House - имя и этажность
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Создание метода go_to с параметром new_floor и
    # логикой внутри него на основе описания задачи
    def go_to(self, new_floor):
        self.new_floor = new_floor
        # Если new_floor больше чем self.number_of_floors или меньше 1,
        # то вывод строки "Такого этажа не существует"
        if int(new_floor) > int(self.number_of_floors) or 1 > int(new_floor):
            print(f'Такого этажа {self.new_floor} не существует в доме "{self.name}"')
            print(f'В доме "{self.name}" не более {self.number_of_floors} этажей')
        # вывод на экран (в консоль) значения от 1 до new_floor(включительно)
        else:
            print(f'Этажи в доме "{self.name}":')
            for i in range(int(new_floor)):
                i += 1
                print(i)

# Исходные данные задачи
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

# Произвольные исходные данные согласно введеных ранее знаений
home = House(gk, maxfloor)
home.go_to(floor)