class SodaBottle:
    brand: str
    volume: float

    def __init__(self, brand, volume):
        self.brand = brand
        self.volume = volume

    def serialize(self) -> str:
        return f"{self.brand};{self.volume}"


