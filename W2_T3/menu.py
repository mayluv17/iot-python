class Menu:
    def askChoice(self) -> int:
        choice = -1
        feed = input("Your choice: ")
        if feed.isdigit():
            choice = int(feed)
        return choice
    def addBottle(self):
        print("'Add bottle' not implemented yet.")
    def showBottle(self):
        print("'Show bottle' not implemented yet.")
    def saveBottle(self):
        print("'Save bottle' not implemented yet.")
    def run(self) -> None:
        choice = -1
        while choice != 0:
            print("Menu:")
            print("1 - Add bottle")
            print("2 - Show bottle")
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
