class Animal:


    def __init__(self, name, age,species):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        print("Какой-то животный звук")

    def info1(self):
        print(f"Кличка: {self.name}, Возраст: {self.age}, Вид: {self.species}")

    def __del__(self):
        print(f"Объект '{self.name}' удалён.")

class Dog(Animal):

    def __init__(self, name, age, species, breed, guard_status):
        super().__init__(name, age, species)
        self.breed = breed
        self.guard_status = guard_status

    def __del__(self):
        pass

    def make_sound(self):
        print("ГАУ ГАУ ГАУ")

    def info2(self):
        print(f"Порода:{self.breed}, Статус охраны дома: {self.guard_status}")