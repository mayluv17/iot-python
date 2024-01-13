from coin_acceptor import CoinAcceptor

print("Program starting.")
print("Welcome to coin acceptor program.")
print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)\n")


def prompt_input() -> None:
    choice = input("Insert coin(0 return, -1 exit): ")
    return choice

def main() -> None:
    coin_acceptor = CoinAcceptor()

    while True:
        choice = prompt_input()

        if choice == "0": 
            print("Returning coins...")
            coin_acceptor.returnCoins()
            print("Inserted coins - 0, value - 0€\n")
            continue 


        if choice == "-1":
            print("Exiting program.\n")
            print("Program ending.")
            break
       
        coin_acceptor.insertCoin(choice)
        (amount, value) =  coin_acceptor.getAmount()
        print(f"Inserted coins - {amount}, value - {value}€\n") 

    return None

if __name__ == "__main__":
    main()


#     Program starting.
# Welcome to coin acceptor program.
# Insert new coin by typing it's value (0 returns the money, -1 exits the program)

# Insert coin(0 return, -1 exit): 2
# Inserting...
# Inserted coins - 1, value - 2.0€

# Insert coin(0 return, -1 exit): 0.5
# Inserting...
# Inserted coins - 2, value - 2.5€

# Insert coin(0 return, -1 exit): 0
# Returning coins...
# 2 coins with 2.5€ value returned.
# Inserted coins - 0, value - 0€

# Insert coin(0 return, -1 exit): 1
# Inserting...
# Inserted coins - 1, value - 1.0€

# Insert coin(0 return, -1 exit): -1
# Exiting program.

# Program ending.