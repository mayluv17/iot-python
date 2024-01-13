from coin_acceptor import CoinAcceptor

print("Program starting.")

def display_options() -> None:
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")
    return None

def main() -> None:
    coin_acceptor = CoinAcceptor()

    while True:
        display_options()
        choice = input("Your choice: ")

        if choice == "1":
            coin_acceptor.insertCoin()
        elif choice == "2":
            print(f"Currently '{coin_acceptor.getAmount()}' coins in coin acceptor\n")
        elif choice == "3":
            returned_coins = coin_acceptor.returnCoins()
            print(f"Coin acceptor returned '{returned_coins}' coins.\n")
        elif choice == "0":
            print("Program ending.")
            break
        else:
            print("Invalid choice. Please try again.")
    return None

if __name__ == "__main__":
    main()