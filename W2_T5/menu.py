class Menu:
    bottles: list = []

    def askChoice(self) -> int:
        choice = -1
        feed = input("Your choice: ")
        if feed.isdigit():
            choice = int(feed)
        return choice
    
    def serialize(self, brand, volume) -> str:
        return f"{brand};{volume}\n"

    def addBottle(self) -> None:
        print("Creating soda bottle.")
        brand: str = input("Insert brand: ")
        volume: str = input("Insert volume: ")
        bottleObject = {"brand": brand, "volume": volume}
        self.bottles.append(bottleObject)
        return None

    def showBottle(self):
        print("#### Soda bottles ####")
        index = 1
        for soda in self.bottles:
            print(f"Bottle {index}:")
            print(f"  brand - {soda['brand']}")
            print(f"  volume - {soda['volume']}")
            index = index + 1

        print("#### Soda bottles ####")

    def saveBottle(self):

        serialized = [self.serialize(bottle['brand'], bottle['volume']) for bottle in self.bottles]
        content = ''.join(serialized)

        with open("inventory.txt", "w") as file:
            file.write(content)

        print("Saving soda bottles...")
        print("Saving completed!")

    def run(self) -> None:
        choice = -1
        while choice != 0:
            print("Menu:")
            print("1 - Add bottle")
            print("2 - Show bottles")
            print("3 - Save bottle")
            print("0 - Exit")
            choice = self.askChoice()
            if choice == 1:
                self.addBottle()
            elif choice == 2:
                self.showBottle()
            elif choice == 3:
                self.saveBottle()
            elif choice == 0:
                pass
            else:
                print("Unknown option, try again.")
            print("")
        return None
