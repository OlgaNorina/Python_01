class Plant:
    """Represent a plant in the garden with its physical attr."""
    name: str
    height: float
    age_days: int

    class _PlantStats:
        """A nested class to track statistics for a plant instance."""
        grow_stat: int
        age_stat: int
        show_stat: int

        def __init__(self) -> None:
            """Initializes a new instance of plant statistics

            Args:
                grow_stat: Number of times the plant has grown.
                age_stat: Number of times the plant has aged.
                show_stat: Number of times the plant has been displayed.
            """
            self.grow_stat = 0
            self.age_stat = 0
            self.show_stat = 0

    def __init__(self, name: str, height: float, age_days: int) -> None:
        """Initialize a new plant instance and apply validation setters.

        Args:
            name (str): The common name of the plant.
            height (float): The starting height in cm.
            age_days (int): The starting age in days.
            stats:
        """
        self.name = name
        self.height = height
        self.age_days = age_days
        self.stats = self._PlantStats()

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        """Check if a given age in days is greater than a year.

        Args:
            age_days (int): The age to check in days.

        Returns:
            bool: True if the age is greater than 365 days, False otherwise.
        """
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        """Create a placeholder Plant instance with default fallback values.

        Returns:
            Plant: A new Plant instance named 'Unknown plant'.
        """
        return cls(name="Unknown plant", height=0.0, age_days=0)

    def show(self) -> None:
        """Create a placeholder Plant instance with default fallback values.

        Returns:
            Plant: Plant instance named 'Unknown plant' and zeroed attributes.
        """
        self.stats.show_stat += 1
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.age_days} days old"
            )

    def age(self, days_count: int = 1) -> None:
        """Advance the plant's age and counter sequentially by one day."""
        self.stats.age_stat += 1
        self.age_days += days_count

    def grow(self, increase_amount: float = 0.1) -> None:
        """Increment the plant's height and update its statistics.

        Args:
            increase_amount: The multiplier factor for the current height.
        """
        self.height = round(self.height * increase_amount, 1)
        self.stats.grow_stat += 1


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

    def show(self) -> None:
        """Display extended details about the flower."""
        super().show()
        print(f" Color: {self.color.lower()}")
        if self.is_blooming:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    """Represent a tree, inheriting basic behaviors from Plant."""
    trunk_diam: float
    is_shade: int

    class _TreeStats(Plant._PlantStats):
        """Extend the internal statistics tracking specifically for Tree."""
        _shade_stat: int

        def __init__(self) -> None:
            """Initializes a new instance of tree statistics.

            Args:
                _shade_stat (int): Number of times the tree has provided shade.
            """
            super().__init__()
            self._shade_stat = 0

    def __init__(self, name: str, height: float,
                 age_days: int, trunk_diam: float) -> None:
        """Initialize a new tree instance.

        Args:
            name: The common name of the tree.
            height: The starting height in cm.
            age_days: The starting age in days.
            trunk_diam: The diameter of the tree trunk in cm.
            stats: The extended tree tracking statistics instance.
        """
        super().__init__(name, height, age_days)
        self.trunk_diam = trunk_diam
        self.is_shade = False
        self.stats: Tree._TreeStats = self._TreeStats()

    def show(self) -> None:
        """Display extended details about the tree."""
        super().show()
        print(f" Trunk diameter: {self.trunk_diam}cm")

    def produce_shade(self) -> None:
        """Enable the tree to cast shade and print the shade coverage."""
        self.is_shade = True
        print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{self.height:.1f}cm long and "
                f"{self.trunk_diam:.1f}cm wide"
                )
        self.stats._shade_stat += 1


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

    def show(self) -> None:
        """Display extended details about the vegetable."""
        super().show()
        print(
            f" Harvest season: {self.harv_season}\n "
            f"Nutritional value: {self.nutrit_val}"
            )

    def grow_nutrit(self, nutrit: int) -> None:
        """Simulate aging and growth across a given day interval.

        Args:
            period: The number of days to process growth cycles.
        """
        self.nutrit_val += nutrit


class Seed(Flower):
    """Represent a seed-producing flower in the garden with seed tracking."""
    current_seeds: int
    max_seeds: int

    def __init__(self, name: str, height: float, age_days: int,
                 color: str, seed_count: int) -> None:
        """Initialize a new seed-producing flower instance.

        Args:
            name (str): The common name of the flower.
            height (float): The starting height in cm.
            age_days (int): The starting age in days.
            color (str): The visual color of the flower petals.
            seed_count (int): The maximum seed capacity for this instance.
        """
        super().__init__(name, height, age_days, color)
        self.current_seeds = 0
        self.max_seeds = seed_count

    def bloom(self) -> None:
        """Trigger the blooming process."""
        super().bloom()
        self.current_seeds = self.max_seeds

    def show(self) -> None:
        """Display the plant's core information and its current seed count."""
        super().show()
        print(f" Seeds: {self.current_seeds}")

    def grow(self, increase_amount: float = 1.375) -> None:
        """Advance the growth cycle of the vegetable.

        Args:
            increase_amount: The factor applied to current height.
        """
        super().grow(increase_amount=increase_amount)


def display_statistics(plant_instance: Plant) -> None:
    """A standalone unique function that prints stats for any plant type.

    It checks if the extra tree attribute exists inside the stats object.
    """
    print(f"[statistics for {plant_instance.name.capitalize()}]")
    print(
        f"Stats: {plant_instance.stats.grow_stat} grow, "
        f"{plant_instance.stats.age_stat} age, "
        f"{plant_instance.stats.show_stat} show"
        )
    if plant_instance.__class__ == Tree:
        print(f" {plant_instance.stats._shade_stat} shade")


if __name__ == "__main__":

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 age_days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
        )
    print(
        f"Is 400 age_days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
        )

    print("\n=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print(f"[asking the {rose.name} to grow and bloom]")
    rose.grow(1.533)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print(f"[make {sunflower.name} grow, age and bloom]")
    sunflower.bloom()
    sunflower.grow(1.375)
    sunflower.age(20)
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)
