from cs50 import SQL
from sys import argv

# Open database for writing
open(f"students.db", "r")
db = SQL("sqlite:///students.db")

# check for house input
if len(argv) != 2:
    print("ERROR")

# obtain rows for house
names = db.execute("SELECT * FROM students WHERE house=? ORDER BY last, first", argv[1])

# print names and births in alphabetical order for that house
for row in names:
    if row["middle"] == None:
        print(row["first"], row["last"] + ',', "born", row["birth"])

    else:
        print(row["first"], row["middle"], row["last"] + ',', "born", row["birth"])
