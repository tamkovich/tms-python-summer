"""
Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""
class President:
    """создан класс Президент"""
    def __init__(self, name, age, sex, party, budget, city, term):

        self.name = name
        self.age = age
        self.sex = sex
        self.__party = party
        self.__budget = budget
        self.__city = city
        self.term = term

    @property
    def party(self):
        return self.__party

    @party.setter
    def party(self, party):
        self.__party = party

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        self.__budget = budget

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    def go_away(self):
        print(f'{self.name} go away!')
        self.budget = 0

    def new_term(self, new_term=True):
        print('elections were held')
        if new_term:
            self.term += 1
        else:
            self.term = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        self.sex = sex

    def get_term(self):
        return self.term

    def set_term(self, term):
        self.term = term


# new_President = President('Lu', 67, 'male', 'KP', 40000, 'Shklov', 1)
# print(new_President.__dict__)
# new_President.new_term(False)
# new_President.go_away()
# new_President.name = "Sveta"
# new_President.party = "Alternate"
# new_President = President('Sveta', 37, 'famale', 'Alternate', 4000, 'Mazir', 1)
# print(new_President.__dict__)

class Footballer:
    """создан класс Футболист"""
    def __init__(self, name, age, sex, nation, club, number, price):

        self.__name = name
        self.__age = age
        self.__sex = sex
        self.nation = nation
        self.club = club
        self.number = number
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    def get_nation(self):
        return self.nation

    def set_nation(self, nation):
        self.nation = nation

    def get_club(self):
        return self.club

    def set_club(self, club):
        self.club = club

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def injury(self):
        print(f'{self.name} get injury!')
        self.price -= 10000

    def out(self):
        print(f'{self.name} left club!')
        self.club = None

    def change_number(self, number):
        self.number = number


# footballer1 = Footballer("Mane", 28, "male", "Senegal", "FC Liverpool", '9', 110000)
# footballer1.injury()
# footballer1.out()
# footballer1.change_number('11')
# print(footballer1.__dict__)
# footballer1.club = 'Real'
# print(footballer1.club)

class CarSell:
    """создан класс Автомобиль на продаже"""
    def __init__(self, mark, model, drive_unit, mileage, fuel, color, price):

        self.__mark = mark
        self.__model = model
        self.__drive_unit = drive_unit
        self.mileage = mileage
        self.fuel = fuel
        self.color = color
        self.price = price

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def drive_unit(self):
        return self.__drive_unit

    @drive_unit.setter
    def drive_unit(self, drive_unit):
        self.__drive_unit = drive_unit

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_fuel(self):
        return self.fuel

    def set_fuel(self, fuel):
        self.fuel = fuel

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def discount(self, discount):  # скидка в процентах
        self.price *= (100-discount)/100

    def change_price(self, price):
        self.price = price


# car1 = CarSell('Tesla', 'model M', '4x4', 300343, "elec.", "white", 50000)
# car1.discount(3)
# print(car1.__dict__)

class House:
    """создан класс дом"""
    def __init__(self, height, width, length, state, numb_floors, years_old, elevators):

        self.__height = height
        self.__width = width
        self.__length = length
        self.state = state
        self.numb_floors = numb_floors
        self.years_old = years_old
        self.elevators = elevators

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_numb_floors(self):
        return self.numb_floors

    def set_numb_floors(self, numb_floors):
        self.numb_floors = numb_floors

    def get_years_old(self):
        return self.years_old

    def set_years_old(self, years_old):
        self.years_old = years_old

    def get_elevators(self):
        return self.elevators

    def set_elevators(self, elevators):
        self.elevators = elevators

    def birthday_house(self):
        self.years_old += 1
        print(f'This house is {self.years_old} years old')
        if self.years_old > 29 and self.state != 'good':
            print("Need major overhaul house")
        elif self.years_old > 120 and self.state == 'bad':
            print("Need destruction house")
        elif self.years_old < 20:
            print("This house is new")
        else:
            pass

    def overhaul(self):
        self.state = 'good'


# house1 = House(150, 30, 50, 'normal', 48, 28, 3)
# print(house1.__dict__)
# house1.birthday_house()
# house1.birthday_house()
# print(house1.state)
# print(house1.years_old)
# house1.overhaul()
# house1.birthday_house()
# print(house1.state)

class WarElf:
    """создан класс боевой ельф"""
    def __init__(self, name, squad, rank, health, power, mana, experience, money):

        self.__name = name
        self.__squad = squad
        self.__rank = rank
        self.health = health
        self.power = power
        self.mana = mana
        self.experience = experience
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def squad(self):
        return self.__squad

    @squad.setter
    def squad(self, squad):
        self.__squad = squad

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        self.__rank = rank

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power

    def get_mana(self):
        return self.mana

    def set_mana(self, mana):
        self.mana = mana

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def damage(self, XP):
        self.health -= XP
        if self.health in [0, 3]:
            print(f'This unit will die soon')
            print(f'This unit have {self.health} XP')
        elif self.health < 1:
            print(f'This unit died')
        else:
            print(f'This unit have {self.health} XP')

    def heal(self, XP):
        if self.health + XP <= 10:
            self.health += XP
        else:
            self.health = 10
        self.money -= XP * 1.5
        print(f'This unit has {self.health} XP now')
        print(f'This unit has {self.money} coins now')

    def attak(self, powerXP=1, manaXP=0):
        self.power -= powerXP
        self.mana -= manaXP
        if self.power == 0:
            print(f"This unit has not power")
        if self.mana == 0:
            print(f"This unit has not mana")
        else:
            print(f"power: {self.power}, mana: {self.mana}")

    def full_recovery(self):
        self.health = 10
        self.power = 100
        self.mana = 100
        self.money -= 10
        print(f'This unit is fully recovered')
        print(f'This unit has {self.money} coins now')

    def battle(self):
        self.experience += 1
        self.money += 5
        if self.experience == 25:
            self.rank = 'middle'
            self.money += 10
        elif self.experience == 50:
            self.rank = 'high'
            self.money += 15
        else:
            pass

    def credit_check(self):
        if self.money >= 0:
            print(f'This unit has not debt')
        elif self.money in [-10, 0]:
            print(f'This unit owes money')
            self.health -= 1
        else:
            self.health = 0
            print(f'This unit died over debt')


# unit1 = WarElf("Farold", 'east-grey', 'middle', 8, 15, 20, 49, 7)
# unit1.battle()
# unit1.damage(3)
# unit1.attak(2, 4)
# unit1.damage(1)
# unit1.heal(5)
# print(unit1.__dict__)
# unit1.battle()
# unit1.heal(5)
# unit1.full_recovery()
# print(unit1.__dict__)
# unit1.attak(2, 1)
