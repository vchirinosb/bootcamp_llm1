"""Lab 3."""

from abc import ABC, abstractmethod

class Person:

    """Person abstract class."""

    def __init__(self, name: str, age: int, city: str):
        self._name = name
        self._age = age
        self._city = city
    
    def __str__(self) -> str:
        return f'{self._name}'
    
    def get_age(self) -> int:
        return self._age
    
    def set_age(self, age) -> None:
        if age >= 0:
            self._age = age
        else:
            print(f'Error to set the age for {self._name}')
    
    def presentarse(self) -> None:
        """Print person introduction."""
        print(f"Hello My name is {self._name}. I am {self._age} years old.")
    
    def cumplir_anios(self) -> None:
        """Turn years old."""
        self._age = self._age + 1
    
    def cambiar_ciudad(self, city: str) -> None:
        """Update city of residence"""
        self._city = city


class Student(Person):

    def __init__(self, name: str, age: int, city: str, study_year: str):
        super().__init__(name, age, city)
        self._study_year = study_year
    
    def estudiar(self) -> None:
        print(f'{self._name} is studying')


class Animal(ABC):

    """Animal abstract class."""

    @abstractmethod
    def hacer_sonido(self) -> None:
        pass


class Dog(Animal):
    
    """Dog class."""

    def hacer_sonido(self) -> None:
        """Print the sound the dog makes."""
        print('Woof!')


class Cat(Animal):
    
    """Cat class."""

    def hacer_sonido(self) -> None:
        """Print the sound the cat makes."""
        print('Meow!')


def hacer_que_suenen(animals: list) -> None:
    """Print the sound of the animals."""
    for animal in animals:
        animal.hacer_sonido()


if __name__ == '__main__':
    """Example execution."""
    # Exercise 1:
    person_1 = Person('Mariano', 19, 'Roma')
    person_2 = Person('Antonio', 22, 'Berlin')
    person_3 = Person('Cinthya', 27, 'Tokio')
    person_1._name = 'Mariano Jose'
    person_2.set_age(23)
    person_3._city = 'Lima'

    # Exercise 2:
    person_1.presentarse()
    person_2.cumplir_anios()
    person_3.cambiar_ciudad('London')

    # Exercise 3:
    person_4 = Student('Victor', 30, 'Lisbon', '2nd year')
    person_4.presentarse()
    person_4.cumplir_anios()
    person_4.cambiar_ciudad('Buenos Aires')
    person_4.estudiar()

    # Exercise 4:
    animals = list()
    animals.append(Dog())
    animals.append(Cat())
    hacer_que_suenen(animals)

    # Exercise 5:
    person_5 = Person('Jose', 21, 'Montevideo')
    print(person_5.get_age())
    person_5.set_age(-1)
    person_5.set_age(24)
    print(person_5.get_age())
