import mysql.connector
import csv

csv_file_path = 'employees_data.csv'


# Connect to MySQL server
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="nensi",
    database="ADBMS"
)


cursor = connection.cursor()



try:

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

    # Commit changes
    connection.commit()
    print("Data divided and stored into new tables successfully.")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
