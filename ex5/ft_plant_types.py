class Plant:
    
    name: str
    height: float
    days: int

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days


    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.days} days old")

    def age(self) -> None:
        self.days += 1

    def grow(self) -> None:
        self.height += 2.1


class Flower(Plant):
    color: str
    is_blomint: bool

    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True
        self.show()

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color.lower()}")
        if self.is_blooming:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(
                    f" {self.name.capitalize()} has not bloomed yet\n"
                    f"[asking the {self.name.lower()} to bloom]"
                    )


class Tree(Plant):
    trunk_diam: float
    is_shade: bool

    def __init__(self, name: str, height: float, days: int, trunk_diam: float) -> None:
        super().__init__(name, height, days)
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

    def __init__(self, name: str, height: float, days: int, harv_season: str) -> None:
        self.harv_season = harv_season
        self.nutrit_val = 0
        super().__init__(name, height, days)


    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harv_season}\n Nutritional value: {self.nutrit_val}")
        if self.nutrit_val == 0:
            print(f"[make {self.name.lower()} grow and age for 20 days]")

    def grow_nutrit(self, period: int) -> None:
        for old in range(1, period + 1):
            super().age()
            super().grow()
            self.nutrit_val += 1
        self.show()

print("=== Garden Plant Types ===")
print("=== Flower")
flower1 = Flower("rose", 15.0, 10, "Red")
flower1.show()
flower1.bloom()

print(f"\n=== Tree")
tree1 = Tree("Oak", 200, 365, 5.0)
tree1.show()
tree1.produce_shade()

print(f"\n=== Vegetable")
vegetable1 = Vegetable("Tomato", 5.0, 10, "April")
vegetable1.show()
vegetable1.grow_nutrit(20)
