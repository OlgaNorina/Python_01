class Plant:
    """
    Args:
            name: plant name
            height: plant height in cm
            age_days: plant age_days"""
    
    name: str
    height: float
    age_days: int

    class _PlantStats:
        """Nested class for statistics"""
        
        grow_stat: int
        age_stat: int
        show_stat: int

        def __init__(self) -> None:
            self.grow_stat = 0
            self.age_stat = 0
            self.show_stat = 0


    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls):
        return cls(name = "Unknown plant", height = 0.0, age_days = 0)

    def show(self) -> None:
        self.show_stat += 1
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.age_days} age_days old")

    def age(self) -> None:
        self.age_stat += 1
        self.age_days += 1

    def grow(self, increase: int) -> None:
        self.grow_stat += 1
        self.height = round(self.height * increase, 1)

    


class Flower(Plant):
    color: str
    is_blomint: bool

    def __init__(self, name: str, height: float, age_days: int, color: str) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color.lower()}")
        if self.is_blooming:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(
                    f" {self.name.capitalize()} has not bloomed yet"
                    )


class Tree(Plant):
    trunk_diam: float
    is_shade: bool

    def __init__(self, name: str, height: float, age_days: int, trunk_diam: float) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diam = trunk_diam
        self.is_shade = False

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diam}cm")
        if self.is_shade == False:
            print(f"[asking the {self.name.lower()} to produce shade]")

    def produce_shade(self) -> None:
        self.is_shade = True
        print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{self.height:.1f}cm long and "
                f"{self.trunk_diam:.1f}cm wide"
                )


class Vegetable(Plant):
    harv_season: str
    nutrit_val: int

    def __init__(self, name: str, height: float, age_days: int, harv_season: str) -> None:
        self.harv_season = harv_season
        self.nutrit_val = 0
        super().__init__(name, height, age_days)


    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harv_season}\n Nutritional value: {self.nutrit_val}")
        if self.nutrit_val == 0:
            print(f"[make {self.name.lower()} grow and age for 20 age_days]")

    def grow_nutrit(self, period: int) -> None:
        for old in range(1, period + 1):
            super().age()
            super().grow()
            self.nutrit_val += 1
        self.show()


class Seed(Flower):
    current_seeds: int
    max_seeds: int

    def __init__(self, name: str, height: float, age_days: int, color: str, seed_count: int) -> None:
        super().__init__(name, height, age_days, color)
        self.current_seeds = 0
        self.max_seeds = seed_count

    def bloom(self) -> None:
        super().bloom()
        self.current_seeds = self.max_seeds

    def show(self) -> None:
        Plant.show()


def get_statistics(self) -> None:
        print(f"[statistics for {self.name.capitalize()}]")
        print(f"Stats: {self.grow_stat} grow, {self.age_stat} age, {self.show_stat} show")

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 age_days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 age_days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")

    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    rose.get_statistics()
    print(f"[asking the {rose.name} to grow and bloom]")
    rose.grow(1.533)
    rose.bloom()
    rose.show()
    rose.get_statistics()
