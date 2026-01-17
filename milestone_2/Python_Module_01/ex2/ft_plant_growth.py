class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_info(self):
        print(f'{self._name}: {self._height}cm , {self._age} days old')

    def grow(self):
        self._height += 1

    def age(self):
        self._age += 1
    
    def week_stimulator(self):
        print(f'=== Day 1 ===')
        self.get_info()
        i = 1
        while i < 7:
            self.grow()
            self.age()
            i += 1
        print(f'=== Day {i} ===')
        self.get_info()
        print(f'growth this week: +{i - 1}cm')

plant = Plant("Rose", 25, 30)
plant.week_stimulator()
