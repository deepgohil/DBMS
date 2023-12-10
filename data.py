import csv
import random
from faker import Faker

# Install the 'Faker' library if you haven't already
# pip install faker

# Function to generate random employee data
def generate_employee_data():
    fake = Faker()
    return {
        'EmployeeID': random.randint(1, 100),
        'FullName': fake.name(),
        'Email': fake.email(),
        'City': fake.city(),
        'Salary': random.randint(50000, 100000)
    }

# Specify the file name
csv_file_path = 'employees_data.csv'

# Generate and write 30 employee records to the CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['EmployeeID', 'FullName', 'Email', 'City', 'Salary']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Generate and write 30 employee records
    for _ in range(30):
        employee_data = generate_employee_data()
        writer.writerow(employee_data)

print(f"CSV file '{csv_file_path}' has been generated.")
