class Plant:
    name: str
    height: float
    age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls):
        retrun cls(name = "Unknown plant", height = 0.0, age_days = 0)

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.age_days} days old")

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


class Seed(Flower):




        #print(f"Is {age_days} days more than a year? -> {age_days > 365}")
