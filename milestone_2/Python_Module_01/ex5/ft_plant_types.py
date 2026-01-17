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
    
    def bloom():
        print(f'{self._name} is blooming beautifully!')
    
    def get_info():
        print(f'{self.name} (Flower): {self._height}cm, {self._age} days, {self._color} color')

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
    
    def produce_shade():
        print(f'{self._name} provides 78 square meters of shade')

    def get_info():
        print(f'{self.name} (Tree): {self._height}cm, {self._age} days, {self._trunk_diameter}cm diameter')

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
    
    def get_info():
        print(f'{self.name} (Vegetable): {self._height}cm, {self._age} days, {self.summer} harvest')
    