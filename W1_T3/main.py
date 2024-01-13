from counter import Counter

def display_options() -> None:
    print("\nOptions:")
    print("1) Add count")
    print("2) Get count")
    print("3) Zero count")
    print("0) Exit program")
    return None

def main() -> None:
    counter:int = Counter()

    print("Program starting.")
    print("Initializing counter...")
    print("Counter initialized.")

    while True:
        display_options()
        choice = input("Choice: ")

        if choice == "1":
            counter.addCount()
            print("Count increased")
        elif choice == "2":
            print(f"Current count '{counter.getCount()}'")
        elif choice == "3":
            counter.zeroCount()
            print("Count zeroed")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

    print("\nProgram ending.")
    return None

if __name__ == "__main__":
    main()
