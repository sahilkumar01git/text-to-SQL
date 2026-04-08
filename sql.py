import sqlite3

connection = sqlite3.connect("company.db")

cursor = connection.cursor()

table_info = """
CREATE TABLE IF NOT EXISTS Student(
NAME VARCHAR(25),
CLASS VARCHAR(25),
SECTION VARCHAR(25),
MARKS INT
)
"""

cursor.execute(table_info)

cursor.execute("""INSERT INTO Student VALUES('krish','7th','E',90)""")
cursor.execute("""INSERT INTO Student VALUES('rohit','10th','B',62)""")
cursor.execute("""INSERT INTO Student VALUES('vishesh','12th','D',45)""")
cursor.execute("""INSERT INTO Student VALUES('sahil','11th','A',98)""")
cursor.execute("""INSERT INTO Student VALUES('sandeep','11th','B',77)""")

print("Inserted records:")

data = cursor.execute("""SELECT * FROM Student""")

for row in data:
    print(row)

connection.commit()

connection.close()