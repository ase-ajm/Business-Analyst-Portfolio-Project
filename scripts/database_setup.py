import sqlite3
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "database", "moonrestaurant.db")
os.makedirs(os.path.join(BASE_DIR, "..", "database"), exist_ok=True)

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS moonrestaurant (
    session_id TEXT PRIMARY KEY,
    user_id TEXT,
    session_date TEXT,
    session_time TEXT,
    user_type TEXT,
    device_type TEXT,
    checkout_type TEXT,
    stage_reached TEXT,
    drop_off_stage TEXT,
    completed_order TEXT,
    items_in_cart INTEGER,
    cart_value_usd REAL,
    time_browse_sec INTEGER,
    time_cart_sec INTEGER,
    time_checkout_sec INTEGER,
    time_payment_sec INTEGER,
    total_session_time_sec INTEGER,
    promo_code_used TEXT,
    payment_method TEXT,
    order_id TEXT,
    order_value_usd REAL
)
""")

DATA_DIR = os.path.join(BASE_DIR, "..", "data")

with open(os.path.join(DATA_DIR, "moonrestaurant_user_behavior.csv"), newline="") as f:
    for row in csv.DictReader(f):
        cursor.execute("INSERT OR IGNORE INTO moonrestaurant VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       (row["session_id"], row["user_id"], row["session_date"], row["session_time"],
                        row["user_type"], row["device_type"], row["checkout_type"], row["stage_reached"],
                        row["drop_off_stage"], row["completed_order"], row["items_in_cart"],
                        row["cart_value_usd"], row["time_browse_sec"], row["time_cart_sec"],
                        row["time_checkout_sec"], row["time_payment_sec"], row["total_session_time_sec"],
                        row["promo_code_used"], row["payment_method"], row["order_id"], row["order_value_usd"]))

connection.commit()
connection.close()
print("Database setup complete")