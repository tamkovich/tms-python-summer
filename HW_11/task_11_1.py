class Quadratic_equation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def derivation_of_an_equation(self):
        print(f'({self.__a}) * x^2 + ({self.__b}) * x + ({self.__c})')

    def finding_roots(self):
        diskr = (self.__b ** 2) - (4 * self.__a * self.__c)
        if diskr > 0:
            x1 = ((-1) * self.__b + diskr) / (2 * self.__a)
            x2 = ((-1) * self.__b - diskr) / (2 * self.__a)
            print(f'Корни уравнения по введённым параметрам: {x1}, {x2}')
            return x1, x2
        elif diskr == 0:
            x = (-1) * self.__b / (2 * self.__a)
            print(f'Уравнение имеет единсственный корень: {x}')
            return x
        elif diskr < 0:
            print('Уравнение не имеет корней')


class Player:

    def __init__(self, name, health, damage, level=1):
        self.__level = level
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    def hit(self, other):
        other.__health -= (self.__damage * 0.6)

    def lvl_up(self):
        self.__health += 15
        self.__damage += 3
        self.__level += 1


class Warrior(Player):
    def __init__(self, name, health, damage, level=1, rage=100):
        super().__init__(name, health, damage, level)
        self.__rage = rage

    @property
    def rage(self):
        return self.__rage

    @rage.setter
    def rage(self, rage):
        self.__rage = rage

    def hero_hit(self, other):
        other.health -= self.damage
        self.__rage -= 3

    def hysteria(self, other):
        other.health -= (self.damage * 1.3)
        self.health -= ((self.damage * 1.3) * 0.3)


class Paladin(Player):
    def __init__(self, name, health, damage, level=1, mana=1000):
        super().__init__(name, health, damage, level)
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, mana):
        self.__mana = mana

    def flash_light(self, other):
        other.health += 10
        self.__mana -= 80

    def light_strike(self, other):
        other.health -= self.damage
        self.__mana -= 25


class Mage(Player):
    def __init__(self, name, health, damage, level=1, mana=1000):
        super().__init__(name, health, damage, level)
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, mana):
        self.__mana = mana

    def mana_burn(self, other):
        other.mana -= 70
        self.__mana -= 33

    def fire_ball(self, other):
        other.health -= self.damage
        self.__mana -= 4


hoor = Warrior('hoor', 160, 17)
ronni = Paladin('ronni', 150, 13)
gon = Mage('gon', 140, 18)

print(gon.__dict__)
print(ronni.__dict__)
print(hoor.__dict__)
gon.mana_burn(ronni)
gon.mana_burn(ronni)
ronni.light_strike(gon)
gon.fire_ball(hoor)
hoor.hero_hit(ronni)
hoor.hysteria(ronni)

print(gon.__dict__)
print(ronni.__dict__)
print(hoor.__dict__)
