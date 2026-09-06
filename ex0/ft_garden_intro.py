"""Module to introduce and display information about a garden plant."""


def ft_garden_intro() -> None:
    """Store and display basic attributes of a single plant."""
    name: str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ==")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days")
    print("\n=== End of Program ==")


if __name__ == "__main__":
    ft_garden_intro()
