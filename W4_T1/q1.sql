CREATE TABLE IF NOT EXISTS device (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mac VARCHAR(12) UNIQUE NOT NULL,
    os TEXT NOT NULL,
    model TEXT NOT NULL
);
