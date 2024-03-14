from soda_bottle import SodaBottle

class Main:
    
    def __init__(self) -> None:
        print("Program starting.")
        filename = input("Insert filename: ")

        try:
            with open(filename, 'r') as file:
               string_from_file = ''.join(file.read().splitlines())
               print(f'Deserializing "{string_from_file}"')

        except FileNotFoundError:
            print(f"File '{filename}' not found.")

        soda_bottle = SodaBottle(string_from_file)
        deserialized_data = soda_bottle.deserialize()
        print(f"Looks like {deserialized_data[1]} litre {deserialized_data[0]} bottle.")
        print("Program ending.")
        return None

if __name__ == "__main__":
    app = Main()