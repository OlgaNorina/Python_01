class Plant:
    name: str
    rise: float
    days: int

    def __init__(self, name: str, rise: float, days: int) -> None:
        self.name = name
        self.rise = rise
        self.days = days

    def show(self) -> None:
        print(f"Created: {self.name}: {self.rise:.1f}cm, {self.days} days old")

    def age(self) -> None:
        self.days += 1

    def grow(self) -> None:
        starting_height: float = self.rise
        print(f"\n{self.name}: {self.rise:.1f}cm, {self.days} days old")
        for day in range(1, 8):
            print(f"== Day {day} ==")
            self.age()
            self.rise = round(self.rise * 1.01, 1)
            print(f"{self.name}: {self.rise:.1f}cm, {self.days} days old")

        progress: float = self.rise - starting_height
        print(f"Growth this week: {progress:.1f}cm")


def main() -> None:
    print("=== Plant Factory Output ===")

    plant1: Plant = Plant("Rose", 25.0, 30)
    plant2: Plant = Plant("Oak", 200.0, 365)
    plant3: Plant = Plant("Cactus", 5.0, 90)
    plant4: Plant = Plant("Sunflower", 80.0, 45)
    plant5: Plant = Plant("Fern", 15.0, 120)

    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()


if __name__ == "__main__":
    main()
