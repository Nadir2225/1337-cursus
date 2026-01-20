class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_info(self):
        print(
            f'Current plant: {self._name} '
            f'({self._height}cm , {self._age} days)'
        )

    def get_age(self):
        return self._age

    def set_age(self, age):
        if (age >= 0):
            self._age = age
            print(f'Age updated: {age} days [OK]')
        else:
            print(f'Invalid operation attempted: age {age} days [REJECTED]')
            print('Security: Negative age rejected')

    def get_height(self):
        return self._height

    def set_height(self, height):
        if (height >= 0):
            self._height = height
            print(f'Height updated: {height}cm [OK]')
        else:
            print(f'Invalid operation attempted: height {height}cm [REJECTED]')
            print('Security: Negative height rejected')


print('=== Garden Security System ===')
secure_plant = SecurePlant("Rose", 19, 16)
print('Plant created: Rose')
secure_plant.set_height(25)
secure_plant.set_age(30)
print()
secure_plant.set_height(-5)
print()
secure_plant.get_info()
