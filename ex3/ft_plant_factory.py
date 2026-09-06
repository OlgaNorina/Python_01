"""Module for streamlining plant instantiation using class constructors."""


class Plant:
    """Represents a plant initialized directly with its starting values."""
    name: str
    height: float
    age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        """Initialize a new plant instance immediately with characteristics.

        Args:
            name (str): The common name of the plant.
            height (float): The starting height of the plant in cm.
            age_days (int): The starting age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        """Display the formatted plant information to the console."""
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.age_days} days old"
            )

    def age(self) -> None:
        """Advance the plant's age by one day."""
        self.age_days += 1

    def grow(self) -> None:
        """Simulate a 7-day growth phase using a constant factor multiplier."""
        starting_height: float = self.height
        for day in range(1, 8):
            print(f"== Day {day} ==")
            self.age()
            self.height = round(self.height * 1.01, 1)
            self.show()

        progress: float = self.height - starting_height
        print(f"Growth this week: {progress:.1f}cm")


def main() -> None:
    """Instantiate and show 5 different plants immediately."""
    print("=== Plant Factory Output ===")

    plant1: Plant = Plant("Rose", 25.0, 30)
    plant2: Plant = Plant("Oak", 200.0, 365)
    plant3: Plant = Plant("Cactus", 5.0, 90)
    plant4: Plant = Plant("Sunflower", 80.0, 45)
    plant5: Plant = Plant("Fern", 15.0, 120)

    print("Created: ", end="")
    plant1.show()
    print("Created: ", end="")
    plant2.show()
    print("Created: ", end="")
    plant3.show()
    print("Created: ", end="")
    plant4.show()
    print("Created: ", end="")
    plant5.show()


if __name__ == "__main__":
    main()
