class Plant:
    name: str
    _height: float
    _age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0

        self.set_height(height)
        self.set_age(age_days)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, value: float) -> None:
        if value < 0:
            print(
                    f"{self.name.capitalize()}: Error, height can't be negative\n"
                    f"Height update rejected"
                    )
        else:
            self._height = float(value)
            print(f"Height updated: {self._height}")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(
                    f"{self.name.capitalize()}: Error, age can't be negative\n"
                    f"Age update rejected"
                    )
        else:
            self._age_days = int(value)
            print(f"Age updated: {self._age_days} days")

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def grow(self) -> None:
        self.set_height(self.get_height() + 1.0)

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self._height:.1f}cm, {self._age_days} days old")

if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("rose", 15.0, 10)
    print("Plant created: ", end = "")
    rose.show()
    print("\n")
    rose.set_height(10.0)
    rose.set_age(20)
    print("\n")

    rose.set_height(-10)
    rose.set_age(-5)

    print("\nCurrent state: ", end = "")
    rose.show()
