'''class Mobil:
    def __init__ (self, model, number):
        self.model = model
        self.number = number

    def info(self):
        print(f'Модель: {self.model} Номер: {self.number}' )

    def call(self):
        print(f'номер {self.number}' )

Mobil1 = Mobil('aal', '777777777')
Mobil1.info()
Mobil1.call()'''

'''class Car:
    def __init__ (self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f'Бренд: {self.brand} Год: {self.year}' )


Car1 = Car('Haval', 2025)
Car2 = Car('Lada', 2007)

print(Car1.brand, Car1.year)
print(Car2.brand, Car2.year)'''

class Calculator:
    def add(self, a,b ):
        return a+b

    def multiply(self, a,b):
        return a*b

    def divide(self, a,b):
        return a/b

    def remainder(self, a,b):
        return a%b

calc = Calculator()
print(calc.add(2,3))
print(calc.multiply(4,5))
print(calc.divide(2,3))
print(calc.remainder(4,5)