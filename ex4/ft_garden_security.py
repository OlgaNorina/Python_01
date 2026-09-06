"""Module for managing garden plant properties with safe setters and getters."""


class Plant:
    """Represents a garden plant with encapsulated attributes and validators."""
    name: str
    _height: float
    _age_days: int
    is_new: bool
     
    def __init__(self, name: str, height: float, age_days: int) -> None:
        """Initialize a new plant instance and apply validation setters.

        Args:
            name (str): The common name of the plant.
            height (float): The starting height in cm (validated safely).
            age_age_days (int): The starting age in days (validated safely).
        """
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self.is_new = True

        self.set_height(height)
        self.set_age(age_days)
        
    def get_height(self) -> float:
        """Retrieve the current encapsulated height of the plant.

        Returns:
            float: The plant's height in centimeters.
        """
        return self._height

    def get_age(self) -> int:
        """Retrieve the current encapsulated age of the plant.

        Returns:
            int: The plant's age in days.
        """
        return self._age_days

    def set_height(self, value: float) -> None:
        """Validate and update the plant's height safely.

        Args:
            value (float): The new height value to apply.
        """
        if value < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            if not self.is_new:
                print(f"Age update rejected")
        else:
            self._height = float(value)
            if not self.is_new:
                print(f"Height updated: {self._height}")

    def set_age(self, value: int) -> None:
        """Validate and update the plant's age safely.

        Args:
            value (int): The new age value to apply in days.
        """
        if value < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            if not self.is_new:
                print(f"Age update rejected")
        else:
            self._age_days = int(value)
            if not self.is_new:
                print(f"Age updated: {self._age_days} age days")
        self.is_new = False

    def age(self) -> None:
        """Advance the plant's age sequentially by one day."""
        self.set_age(self.get_age() + 1)

    def grow(self) -> None:
        """Increment the plant's height sequentially by one centimeter."""
        self.set_height(self.get_height() + 1.0)

    def show(self) -> None:
        """Display the formatted encapsulated plant state summary."""
        print(
            f"{self.name.capitalize()}: "
            f"{self._height:.1f}cm, {self._age_days} days old"
            )

if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("rose", 15.0, 10)
    print("Plant created: ", end = "")
    rose.show()
    print("\n")
    rose.set_height(25.0)
    rose.set_age(30)
    print("\n")
    rose.set_height(-10)
    rose.set_age(-5)
    print("\nCurrent state: ", end = "")
    rose.show()
    print("\n")
    
    sunflower = Plant("sunflower", 70.0, -60)
