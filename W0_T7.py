class Main:
   try:
    userInput: str = input("Insert number: ")
    print("Inserted value is '{}'".format(float(userInput)))
   except Exception:
      print("Oops! That wasn't valid number.")

if __name__ == "__main__":
    app = Main()


# Insert number: 1
# Inserted value is '1.0'

# Insert number: a
# Oops! That wasn't valid number.