class Plant:
    """Represent a plant in the garden with its physical attributes."""
    name: str
    height: float
    age_days: int

    class _PlantStats:
        """A nested class to track interaction statistics for a plant instance."""
        grow_stat: int
        age_stat: int
        show_stat: int

        def __init__(self) -> None:
            """Initializes a new instance of plant statistics with zeroed counters 
                    
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
        """Check if a given age in days is greater than a standard calendar year.

        Args:
            age_days (int): The age to check in days.

        Returns:
            bool: True if the age is greater than 365 days, False otherwise.
        """
        return age_days > 365

    @classmethod
    def create_anonymous(cls):
        """Create a placeholder Plant instance with default fallback values.

        Returns:
            Plant: A new Plant instance named 'Unknown plant' with zeroed attributes.
        """
        return cls(name = "Unknown plant", height = 0.0, age_days = 0)

    def show(self) -> None:
        """Create a placeholder Plant instance with default fallback values.

        Returns:
            Plant: A new Plant instance named 'Unknown plant' with zeroed attributes.
        """
        self.stats.show_stat += 1
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.age_days} days old")

    def age(self) -> None:
        """Advance the plant's age and counter sequentially by one day."""
        self.stats.age_stat += 1
        self.age_days += 1

    def grow(self, increase_amount: float = 0.1) -> None:
        """Increment the plant's height and update its growth tracking statistics.

        Args:
            increase_amount (float): The multiplier factor applied to the current 
                height. Defaults to 0.1.
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

    def grow(self, increase_amount: float = 1.15) -> None:
        """Advance the growth cycle of the flower using a specific scaling multiplier.

        Args:
            increase_amount (float): The multiplier factor applied to current height. 
            Defaults to 1.15.
        """
        super().grow(increase_amount=increase_amount)

    def show(self) -> None:
        """Display extended details about the flower."""
        super().show()
        print(f" Color: {self.color.lower()}")
        if self.is_blooming:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(
                    f" {self.name.capitalize()} has not bloomed yet"
 #                   f"[asking the {self.name.lower()} to bloom]"
                    )


class Tree(Plant):
    """Represent a tree, inheriting basic behaviors from Plant."""
    trunk_diam: float
    is_shade: int
    
    class _TreeStats(Plant._PlantStats):
        """Extend the internal statistics tracking specifically for Tree behaviors."""
        _shade_stat: int
        
        def __init__(self) -> None:
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

    def grow(self, increase_amount: float = 1.01) -> None:
        """Advance the growth cycle of the tree using a specific scaling multiplier.

        Args:
            increase_amount (float): The multiplier factor applied to current height. 
            Defaults to 1.15.
        """
        super().grow(increase_amount=increase_amount)

    def show(self) -> None:
        """Display extended details about the tree."""
        super().show()
        print(f" Trunk diameter: {self.trunk_diam}cm")
 #       if not self.is_shade:
 #           print(f"[asking the {self.name.lower()} to produce shade]")

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

    def grow(self, increase_amount: float = 1.119) -> None:
        """Advance the growth cycle of the vegetable using a specific scaling multiplier.

        Args:
            increase_amount (float): The multiplier factor applied to current height. 
            Defaults to 1.119.
        """
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
        super().show()
        #improve


def display_statistics(plant_instance: Plant) -> None:
    """A standalone unique function that prints stats for any plant type.
    
    It checks dynamically if the extra tree attribute exists inside the stats object.
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
    print(f"Is 30 age_days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 age_days more than a year? -> {Plant.is_older_than_year(400)}")

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
    sunflower = Flower("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    #add seed
