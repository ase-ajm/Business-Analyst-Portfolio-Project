import sqlite3
import os

# Build absolute path to database so script works when called from any directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "database", "bitesandco.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute("""
SELECT 
CASE
    WHEN substr(session_date, -4) < '2025' THEN 'AS-IS'
    ELSE 'TO-BE'
END AS period,
COUNT(*) as total_sessions,
COUNT(CASE WHEN completed_order = 'Yes' THEN 1 END) as completed_orders
FROM bitesandco
GROUP BY period
ORDER BY total_sessions DESC;

""")

for row in cursor.fetchall():
    print(row)

connection.close()


