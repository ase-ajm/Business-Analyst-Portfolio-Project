import sqlite3
import os

# Build absolute path to database so script works when called from any directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "database", "moonrestaurant.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("""
SELECT drop_off_stage, COUNT(*) as total
FROM moonrestaurant
GROUP BY drop_off_stage
ORDER BY total DESC;

""")

for row in cursor.fetchall():
    print(row)

connection.close()


