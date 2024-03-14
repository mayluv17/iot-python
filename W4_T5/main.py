from db_conn import DB_CONN
from product import User_input

PRODUCT_TABLE_STATEMENT = """CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    cost REAL NOT NULL,
    price REAL NOT NULL
);"""

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        DB_CONN.execute(PRODUCT_TABLE_STATEMENT);
        DB_CONN.commit()
        user_input = User_input()
        user_input.prompt_user()
        return None

if __name__ == "__main__":
    app = Main()