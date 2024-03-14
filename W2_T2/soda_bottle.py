class SodaBottle:
    brand: str
    volume: float
    string_from_file: str

    def __init__(self, string):
        self.string_from_file = string


    def deserialize(self) -> list[str]:
        return self.string_from_file.split(";")


