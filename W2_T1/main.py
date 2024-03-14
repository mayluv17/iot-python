from soda_bottle import SodaBottle

class Main:
    
    def __init__(self) -> None:
        print("Program starting.")
        print("Constructing soda bottle.")
        brand = input("Insert brand: ")
        volume = float(input("Insert volume: "))
        soda_bottle = SodaBottle(brand, volume)
        print("SodaBottle object created!")
        print("Serializing SodaBottle object.")
        serialized_data = soda_bottle.serialize()
        print(f"Serialized sodabottle:\n{serialized_data}")
        print("Program ending.")

        return None

if __name__ == "__main__":
    app = Main()