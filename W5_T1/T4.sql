CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    price_per_kilo NUMERIC NOT NULL
);


INSERT INTO product (name, price_per_kilo) VALUES
('Apples', 2.99),
('Bananas', 1.99),
('Oranges', 3.49);

CREATE TABLE receipt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cashier TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);




CREATE TABLE product_receipt (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    receipt_id INTEGER,
    product_id INTEGER,
    amount NUMERIC,
    FOREIGN KEY (receipt_id) REFERENCES receipt(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);
