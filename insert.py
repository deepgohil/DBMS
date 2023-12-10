# import mysql.connector
# from faker import Faker

# # Install the 'Faker' library if you haven't already
# # pip install faker

# # Replace these variables with your actual database information
# host="127.0.0.1",
# user="root",
# password="nensi",
# database="ADBMS"

# # Connect to the MySQL server
# connection = mysql.connector.connect(
#     host=host,
#     database=database,
#     user=user,
#     password=password
# )

# # Create a cursor object to interact with the database
# cursor = connection.cursor()

# # Create the table if it doesn't exist
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS employees (
#     employee_id INT AUTO_INCREMENT PRIMARY KEY,
#     full_name VARCHAR(255),
#     email VARCHAR(255),
#     city VARCHAR(255)
# )
# '''
# cursor.execute(create_table_query)

# # Generate and insert 50 sets of dummy data
# fake = Faker()
# for _ in range(50):
#     dummy_data = {
#         'full_name': fake.name(),
#         'email': fake.email(),
#         'city': fake.city()
#     }

#     insert_query = "INSERT INTO employees (full_name, email, city) VALUES (%s, %s, %s)"
#     cursor.execute(insert_query, (dummy_data['full_name'], dummy_data['email'], dummy_data['city']))

# # Commit the changes to the database
# connection.commit()

# # Close the cursor and connection
# cursor.close()
# connection.close()










import mysql.connector

# Connect to MySQL server
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="nensi",
    database="ADBMS"
)


cursor = connection.cursor()



try:

    cursor.execute('')

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
