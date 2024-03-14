from menu import Menu

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        _menu = Menu()
        _menu.run()
        print("Exiting program.")
        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()