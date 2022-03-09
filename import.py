import csv
from cs50 import SQL
from sys import argv

# set value db equal to our sql database students.db
db = SQL("sqlite:///students.db")

# only accept two arguments for import including characters.csv
if len(argv) != 2:
    print("ERROR")
    exit(1)

# Open csv file and read into database
with open(argv[1], 'r') as student_data:

    # Use DictReader
    reader = csv.DictReader(student_data, delimiter=",")

    for row in reader:

        space_count = 0
        srt_of_name = 0
        for i in range(len(row["name"])):

            if row["name"][i] == ' ':

                space_count += 1
                if space_count == 1:
                    first_name = row["name"][0:i]
                    srt_of_name = i + 1

                elif space_count == 2:
                    middle_name = row["name"][srt_of_name:i]

                    srt_of_name = i + 1

            elif i == len(row["name"]) - 1:

                last_name = row["name"][srt_of_name:i + 1]

                if space_count == 1:
                    middle_name = None
                    
                # All values for a row must be inserted at the same time so we dont get redundant rows
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", 
                           first_name, middle_name, last_name, row["house"], row["birth"])