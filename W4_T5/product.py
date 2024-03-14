from db_conn import DB_CONN
cursor = DB_CONN.cursor()

class User_input:

    def prompt_user(self):
        print("Insert product details below:")
        manufacturer: str = input("- Insert manufacturer: ")
        brand: str = input("- Insert brand: ")
        cost = float(input("- Insert cost: "))
        price = float(input("- Insert price: "))

        cursor.execute('''INSERT INTO product (manufacturer, brand, cost, price)
                        VALUES (?, ?, ?, ?)''', (manufacturer, brand, cost, price))

        DB_CONN.commit()
        print("Storing product details into the database...")
        # DB_CONN.close()
        print("Program ending.")