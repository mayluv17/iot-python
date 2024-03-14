# main.py

from person import Person

class Main:

    def __init__(self) -> None:
        print("Program starting.")
        print("Creating person...")

        john_doe = Person("John", "Doe", 30)

        print("Person created.")
        
        print("Name:", john_doe.getFullname())
        print("Age:", john_doe.getAge())
        
        print("Person has now birthday...")
        
        john_doe.ageUp()
        
        print(f"New age: {john_doe.getAge()}")
        print("Program ending.")
        return None

if __name__ == "__main__":
    app = Main()
