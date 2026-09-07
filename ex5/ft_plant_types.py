"""Module for managing specialized garden plant types using OOP inheritance."""


class Plant:
    """Represent a plant in the garden with its physical attributes."""
    name: str
    height: float
    age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        """Initialize a new plant instance and apply validation setters.

        Args:
            name (str): The common name of the plant.
            height (float): The starting height in cm.
            age_days (int): The starting age in days.
        """
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        """Display the formatted details of the plant."""
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.age_days} days old"
            )

    def age(self) -> None:
        """Advance the plant's age sequentially by one day."""
        self.age_days += 1

    def grow(self, increase_amount: float = 0.1) -> None:
        """Increment the plant's height sequentially in centimeters."""
        self.height = round(self.height * increase_amount, 1)


class Flower(Plant):
    """Represent a flower, inheriting basic behaviors from Plant."""
    color: str
    is_blomint: bool

    def __init__(self, name: str, height: float,
                 age_days: int, color: str) -> None:
        """Initialize a new flower instance.

        Args:
            name: The common name of the flower.
            height: The starting height in cm.
            age_days: The starting age in days.
            color: The color of the flower.
        """
        super().__init__(name, height, age_days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """Trigger the flower to bloom and display its updated status."""
        self.is_blooming = True
        self.show()

    def grow(self, increase_amount: float = 1.15) -> None:
        super().grow(increase_amount=increase_amount)

    def show(self) -> None:
        """Display extended details about the flower."""
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
    """Represent a tree, inheriting basic behaviors from Plant."""
    trunk_diam: float
    is_shade: bool

    def __init__(self, name: str, height: float,
                 age_days: int, trunk_diam: float) -> None:
        """Initialize a new tree instance.

        Args:
            name: The common name of the tree.
            height: The starting height in cm.
            age_days: The starting age in days.
            trunk_diam: The diameter of the tree trunk in cm.
        """
        super().__init__(name, height, age_days)
        self.trunk_diam = trunk_diam
        self.is_shade = False

    def grow(self, increase_amount: float = 1.01) -> None:
        super().grow(increase_amount=increase_amount)

    def show(self) -> None:
        """Display extended details about the tree."""
        super().show()
        print(f" Trunk diameter: {self.trunk_diam}cm")
        if not self.is_shade:
            print(f"[asking the {self.name.lower()} to produce shade]")

    def produce_shade(self) -> None:
        """Enable the tree to cast shade and print the shade coverage."""
        self.is_shade = True
        print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{self.height:.1f}cm long and "
                f"{self.trunk_diam:.1f}cm wide"
                )


class Vegetable(Plant):
    """Represent a vegetable plant, inheriting basic behaviors from Plant."""
    harv_season: str
    nutrit_val: int

    def __init__(self, name: str, height: float,
                 age_days: int, harv_season: str) -> None:
        """Initialize a new vegetable instance.

        Args:
            name: The common name of the vegetable.
            height: The starting height in cm.
            age_days: The starting age in days.
            harv_season: The optimal harvest season.
        """
        self.harv_season = harv_season
        self.nutrit_val = 0
        super().__init__(name, height, age_days)

    def grow(self, increase_amount: float = 1.119) -> None:
        super().grow(increase_amount=increase_amount)

    def show(self) -> None:
        """Display extended details about the vegetable."""
        super().show()
        print(
            f" Harvest season: {self.harv_season}\n "
            f"Nutritional value: {self.nutrit_val}"
            )
        if self.nutrit_val == 0:
            print(f"[make {self.name.lower()} grow and age for 20 days]")

    def grow_nutrit(self, period: int) -> None:
        """Simulate aging and growth across a given day interval.

        Args:
            period: The number of days to process growth cycles.
        """
        for old in range(1, period + 1):
            self.age()
            self.grow()
            self.nutrit_val += 1


if __name__ == "__main__":

    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower1 = Flower("rose", 15.0, 10, "Red")
    flower1.show()
    flower1.bloom()

    print("\n=== Tree")
    tree1 = Tree("Oak", 200, 365, 5.0)
    tree1.show()
    tree1.produce_shade()

    print("\n=== Vegetable")
    vegetable1 = Vegetable("Tomato", 5.0, 10, "April")
    vegetable1.show()
    vegetable1.grow_nutrit(20)
    vegetable1.show()
