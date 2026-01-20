class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_info(self):
        print(f'{self._name} (Plant): {self._height}cm , {self._age} days')


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self):
        print(f'{self._name} is blooming beautifully!')

    def get_info(self):
        print(
            f'{self._name} (Flower): {self._height}cm, '
            f'{self._age} days, {self._color} color'
        )


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f'{self._name} provides 78 square meters of shade')

    def get_info(self):
        print(
            f'{self._name} (Tree): {self._height}cm, '
            f'{self._age} days, {self._trunk_diameter}cm diameter'
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(
            f'{self._name} (Vegetable): '
            f'{self._height}cm, {self._age} days, '
            f'{self.harvest_season} harvest'
        )


print('=== Garden Plant Types ===\n')

rose = Flower('Rose', 25, 30, 'red')
oak = Tree('Oak', 500, 1825, 50)
tomato = Vegetable('Tomato', 80, 90, 'summer', 'Tomato is rich in vitamin C')

rose.get_info()
rose.bloom()
print()
oak.get_info()
oak.produce_shade()
print()
tomato.get_info()
print(tomato.nutritional_value)
