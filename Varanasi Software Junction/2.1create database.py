import sqlite3
import pandas as pd

# Create (or open) a database file
con = sqlite3.connect("shop.db")

# Create tables + sample data
con.executescript("""
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers(
  customer_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT NOT NULL
);

CREATE TABLE orders(
  order_id INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  amount REAL NOT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers(name, city) VALUES
('Asha', 'Varanasi'),
('Ravi', 'Lucknow'),
('Neha', 'Delhi');

INSERT INTO orders(customer_id, amount, created_at) VALUES
(1, 399.0, '2026-01-10'),
(1, 1200.5,'2026-01-18'),
(2, 250.0, '2026-01-12'),
(3, 999.0, '2026-01-20');
""")

con.commit()
con.close()