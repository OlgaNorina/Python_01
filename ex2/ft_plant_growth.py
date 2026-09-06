"""Module for simulating a week of growth and aging for garden plants."""


class Plant:
    """Represents a plant capable of growing and aging over time."""
    name: str
    height: float
    age_days: int

    def __init__(self, name: str, height: float, age_days: int) -> None:
        """Initialize a new plant instance.

        Args:
            name (str): The common name of the plant.
            height (float): The current height of the plant in cm.
            age_days (int): The current age of the plant in days.
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

    def grow(self, weather: str) -> None:
        """Calculate and update plant growth based on weather conditions.

        Args:
            weather (str): Current weather type ("Sunny", "Rainy", "Cloudy").
        """
        factor: float = 1.0

        if weather == "Sunny" and self.name == "Rose":
            factor = 1.05
        elif weather == "Rainy" and self.name == "Rose":
            factor = 1.03
        elif weather == "Cloudy" and self.name == "Rose":
            factor = 1.02
        elif weather == "Sunny" and self.name == "Cactus":
            factor = 1.03
        elif weather == "Rainy" and self.name == "Cactus":
            factor = 1.02
        elif weather == "Cloudy" and self.name == "Cactus":
            factor = 1.01
        elif weather == "Sunny":
            factor = 1.04
        elif weather == "Rainy":
            factor = 1.02
        elif weather == "Cloudy":
            factor = 1.01
        else:
            factor = 1.01

        self.height = round(self.height * factor, 1)

    def weekly_process(self) -> None:
        """Run a 7-day environmental simulation and summarize results."""
        start_height: float = self.height
        forecast: list[str] = ["Sunny", "Rainy", "Cloudy"]
        indices_range = range(3)

        for day in range(1, 8):
            forecast_imitation: int = (day * 1103515245 + 12345) % 2147483648
            index: int = indices_range[forecast_imitation % 3]
            current_weather: str = forecast[index]
            print(f"== Day {day} in {current_weather} weather ==")
            self.age()
            self.grow(current_weather)
            self.show()

        progress: float = self.height - start_height
        print(f"Growth this week: {progress:.1f}cm")


def main() -> None:
    """Execute the simulation registry for multiple plant types."""
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30)
    rose.show()
    rose.weekly_process()

    print("\n=== Garden Plant Growth ===")
    cactus = Plant("Cactus", 10.5, 300)
    cactus.show()
    cactus.weekly_process()

    print("\n=== Garden Plant Growth ===")
    cactus = Plant("narcissus", 10.5, 25)
    cactus.show()
    cactus.weekly_process()


if __name__ == "__main__":
    main()
