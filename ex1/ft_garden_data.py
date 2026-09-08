"""Module for managing and displaying basic garden plant information."""


class Plant:
    """Represent a plant in the garden with its physical attributes."""
    name: str
    height: int
    age: int

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new plant instance.
        Args:
            name (str): The common name of the plant
            height (int): The current height of the plant in cm
            age (int): The age of the plant in days
        """
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        """Display the formatted plant information to the console."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Execute the main garden registry program."""
    print("=== Garden Plant Registry ===")
    plant1: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Sunflower", 80, 45)
    plant3: Plant = Plant("Cactus", 15, 120)

    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    main()
