import sqlite3
import os

# Build absolute path to database so script works when called from any directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "database", "bitesandco.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("""
SELECT device_type, COUNT(*) as total
FROM bitesandco
WHERE completed_order = 'No'
GROUP BY device_type
ORDER BY total DESC;
               
""")

for row in cursor.fetchall():
    print(row)

connection.close()


