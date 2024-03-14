# from db_conn import DB_CONN
# cursor = DB_CONN.cursor()

# class User_input:

#     def askChoice(self) -> int:
#         while True:
#             print("Options:")
#             print("1 - Add product")
#             print("2 - Show products")
#             print("0 - Exit")

#             choice = input("Your choice: ")

#             if choice == '1':
#                 self.add_product()
#             elif choice == '2':
#                 self.show_products()
#             elif choice == '0':
#                 print("Program ending.")
#                 DB_CONN.close()
#                 exit()
#             else:
#                 print("Invalid choice. Please try again.")

#     def add_product(self):
#         print("Insert product details below:")
#         manufacturer = input("- Insert manufacturer: ")
#         brand = input("- Insert brand: ")
#         cost = float(input("- Insert cost: "))
#         price = float(input("- Insert price: "))

#         cursor.execute('''INSERT INTO product (manufacturer, brand, cost, price)
#                         VALUES (?, ?, ?, ?)''', (manufacturer, brand, cost, price))

#         DB_CONN.commit()
#         print("Adding product...")
#         print("Product added!\n")

#     def show_products(self):
#         cursor.execute('''SELECT id, manufacturer, brand, cost, price FROM product''')
#         products = cursor.fetchall()

#         if not products:
#             print("No products found.")
#         else:
#             print("No., Manufacturer, Brand, Cost, Price")
#             for product in products:
#                 print("{}, {}, {}, {}, {}".format(product[0], product[1], product[2], product[3], product[4]))
#         print("\n")

from product import Product
from db_conn import DB_CONN
class MenuProduct:
    def __init__(self):
        pass

    def askChoice(self) -> int:
        choice = int(input("Your choice: "))
        return choice

    def showOptions(self) -> None:
        print("Options:")
        print("1 - Add product")
        print("2 - Show products")
        print("0 - Exit")

    def run(self) -> None:
        while True:
            self.showOptions()
            choice = self.askChoice()
            if choice == 1:
                self.addProduct()
            elif choice == 2:
                self.showProducts()
            elif choice == 0:
                print("Program ending.")
                DB_CONN.close()
                break
            else:
                print("Invalid choice. Please try again.")

    def addProduct(self) -> None:
        print("Insert product details below:")
        manufacturer = input("- Insert manufacturer: ")
        brand = input("- Insert brand: ")
        cost = float(input("- Insert cost: "))
        price = float(input("- Insert price: "))
        product = Product(manufacturer, brand, cost, price)
        product.insertDB()
        print("Adding product...")
        print("Product added!\n")

    def showProducts(self):
        products = Product.queryProducts()
        if not products:
            print("No products found.")
        else:
            print("No., Manufacturer, Brand, Cost, Price")

            for index, product in enumerate(products, 1):
                print("{}, {}, {}, {}, {}".format(index, product.manufacturer, product.brand, product.cost, product.price))
        print("\n")        