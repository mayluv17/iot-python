# from db_conn import DB_CONN
# from menu_product import User_input

# PRODUCT_TABLE_STATEMENT = """CREATE TABLE IF NOT EXISTS product (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     manufacturer VARCHAR(255) NOT NULL,
#     brand VARCHAR(255) NOT NULL,
#     cost REAL NOT NULL,
#     price REAL NOT NULL
# );"""

# class Main:
#     def __init__(self) -> None:
#         print("Program starting.")
#         DB_CONN.execute(PRODUCT_TABLE_STATEMENT);
#         DB_CONN.commit()
#         user_input = User_input()
#         user_input.askChoice()
#         return None

# if __name__ == "__main__":
#     app = Main()


from menu_product import MenuProduct
from db_conn import DB_CONN

PRODUCT_TABLE_STATEMENT = """CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    cost REAL NOT NULL,
    price REAL NOT NULL
);"""

class Main:
    def __init__(self):
        DB_CONN.execute(PRODUCT_TABLE_STATEMENT);
        DB_CONN.commit()
        pass

    def run(self):
        print("Program starting.")
        menu = MenuProduct()
        menu.run()


if __name__ == "__main__":
    main = Main()
    main.run()