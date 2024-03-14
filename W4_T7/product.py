from db_conn import DB_CONN
cursor = DB_CONN.cursor()

class Product:
    def __init__(self, manufacturer, brand, cost, price):
        # self.product_id = product_id
        self.manufacturer = manufacturer
        self.brand = brand
        self.cost = cost
        self.price = price

    def insertDB(self):
        cursor = DB_CONN.cursor()
        cursor.execute('''INSERT INTO product (manufacturer, brand, cost, price)
                        VALUES (?, ?, ?, ?)''', (self.manufacturer, self.brand, self.cost, self.price))
        DB_CONN.commit()

    @staticmethod
    def queryProducts(products=[]):
        cursor = DB_CONN.cursor()
        cursor.execute('''SELECT manufacturer, brand, cost, price FROM product''')
        rows = cursor.fetchall()
        for row in rows:
            products.append(Product(row[0], row[1], row[2], row[3]))
        return products
    
    @staticmethod
    def createProduct() -> 'Product':
        # cursor = DB_CONN.cursor()
        # cursor.execute('''SELECT manufacturer, brand, cost, price FROM product''')
        # rows = cursor.fetchall()
        # for row in rows:
        #     products.append(Product(row[0], row[1], row[2], row[3]))
        return Product.queryProducts()