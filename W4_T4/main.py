from db_conn import DB_CONN
# cursor = DB_CONN.cursor()

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
        print("Program ending.")
        DB_CONN.close()
        return None

if __name__ == "__main__":
    app = Main()