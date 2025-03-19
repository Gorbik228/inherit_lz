from inherit import Animal
from inherit import Dog

def main():
    first = Animal("Мухтар", 5, "Собака")
    second = Dog("Мухтар", 5, "Собака", "Немецкая овчарка", "Охраняет")
    first.make_sound()
    first.info1()
    second.info2()
if __name__ == '__main__': 
    main()
    