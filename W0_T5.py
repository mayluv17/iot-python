class Main:
    currentValue = 0.0

    @staticmethod
    def promptUser(currentValue):
        print("Current value {}".format(currentValue))
        user_input = input("Add number(empty stops): ")
        return user_input

    def __init__(self) -> None:
        while True:
            new_input = self.promptUser(self.currentValue)
            if not new_input:
                print("Final value {}".format(self.currentValue))
                break
            self.currentValue += float(new_input)

if __name__ == "__main__":
    app = Main()

#     Current value 0.0
# Add number(empty stops): 1
# Current value 1.0
# Add number(empty stops): 2
# Current value 3.0
# Add number(empty stops): 
# Final value 3.0
    