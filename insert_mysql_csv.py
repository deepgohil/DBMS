import csv
import mysql.connector

# Replace these variables with your actual database information
host="127.0.0.1",
user="root",
password="nensi",
database="ADBMS"

# Specify the file name
csv_file_path = 'employees_data.csv'  # Update with your CSV file path

# Connect to the MySQL server
connection = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the table if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS EMP (
    ID VARCHAR(20) PRIMARY KEY,
    FullName VARCHAR(20),
    Email VARCHAR(20),
    City VARCHAR(20),
    Salary VARCHAR(5)
)
'''
cursor.execute(create_table_query)

# Read data from the CSV file and insert into the table
with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        insert_query = "INSERT INTO EMP (ID, FullName, Email, City, Salary) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (
            row['EmployeeID'],
            row['FullName'],
            row['Email'],
            row['City'],
            row['Salary']
        ))

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
