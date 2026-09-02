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

    def grow(self, weather: str) -> None:
        factor: float = 1.0

        if weather == "Sunny":
            factor = 1.05
        elif weather == "Rainy":
            factor = 1.03
        elif weather == "Cloudy":
            factor = 1.02

        self.height = round(self.height * factor, 1)

    def daily_process(self, weather: str) -> None:
        self.age()
        self.grow(weather)

    def simulate_week(self) -> None:
        start_height: float = self.height
        weather_options: list[str] = ["Sunny", "Rainy", "Cloudy"]
        indices_range = range(3)

        for day in range(1, 8):
            random_imitation: int = (day * 1103515245 + 12345) % 2147483648
            index: int = indices_range[random_imitation % 3]
            current_weather: str = weather_options[index]
            print(f"== Day {day} in {current_weather} weather ==")
            self.daily_process(current_weather)
            self.show()

        progress: float = self.height - start_height
        print(f"Growth this week: {progress: .1f}cm")


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose: Plant = Plant("Rose", 25.0, 30)
    rose.show()
    rose.simulate_week()


if __name__ == "__main__":
    main()
