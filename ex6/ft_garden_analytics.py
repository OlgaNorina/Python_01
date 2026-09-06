class Plant:
    name: str
    height: float
    age_days: int
    grow_stat: int
    age_stat: int
    show_stat: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.grow_stat = 0
        self.age_stat = 0
        self.show_stat = 0

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls):
        return cls(name = "Unknown plant", height = 0.0, age_days = 0)

    def show(self) -> None:
        self.show_stat += 1
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.age_days} days old")

    def age(self) -> None:
        self.age_stat += 1
        self.days += 1

    def grow(self, increase: int) -> None:
        self.grow_stat += 1
        self.height = round(self.height * increase, 1)

    def get_statistics(self) -> None:
        print(f"[statistics for {self.name.capitalize()}]")
        print(f"Stats: {self.grow_stat} grow, {self.age_stat} age, {self.show_stat} show")


class Flower(Plant):
    color: str
    is_blomint: bool

    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
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




if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")

    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    rose.get_statistics()
    print(f"[asking the {rose.name} to grow and bloom]")
    rose.grow(1.533)
    rose.bloom()
    rose.show()
    rose.get_statistics()
