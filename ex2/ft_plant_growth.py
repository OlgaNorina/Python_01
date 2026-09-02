class Plant:
    name: str
    height: float
    days_old: int

    def __init__(self, name: str, height: float, days_old: int) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

    def age(self) -> None:
        self.days_old += 1

    def grow(self, weather: str, name: str) -> None:
        factor: float = 1.0

        if weather == "Sunny" and name == "Rose":
            factor = 1.05
        elif weather == "Rainy" and name == "Rose":
            factor = 1.03
        elif weather == "Cloudy" and name == "Rose":
            factor = 1.02
        elif weather == "Sunny" and name == "Cactus":
            factor = 1.03
        elif weather == "Rainy" and name == "Cactus":
            factor = 1.02
        elif weather == "Cloudy" and name == "Cactus":
            factor = 1.01

        self.height = round(self.height * factor, 1)

    def daily_process(self, weather: str, name: str) -> None:
        self.age()
        self.grow(weather, name)

    def simulate_week(self, name: str) -> None:
        start_height: float = self.height
        weather_options: list[str] = ["Sunny", "Rainy", "Cloudy"]
        indices_range = range(3)

        for day in range(1, 8):
            random_imitation: int = (day * 1103515245 + 12345) % 2147483648
            index: int = indices_range[random_imitation % 3]
            current_weather: str = weather_options[index]
            print(f"== Day {day} in {current_weather} weather ==")
            self.daily_process(current_weather, name)
            self.show()

        progress: float = self.height - start_height
        print(f"Growth this week: {progress: .1f}cm")


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose: Plant = Plant("Rose", 15.0, 60)
    rose.show()
    rose.simulate_week("Rose")

    print("\n=== Garden Plant Growth ===")
    cactus: Plant = Plant("Cactus", 10.5, 300)
    cactus.show()
    cactus.simulate_week("Cactus")


if __name__ == "__main__":
    main()
