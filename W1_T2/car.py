class Car:
    engine_on: bool
    color: str
    def __init__(self, color) -> None:
        self.engine_on = False
        self.color = color
        return None

    def start(self) -> None:
        print(f"{self.color} car started.")
        return None