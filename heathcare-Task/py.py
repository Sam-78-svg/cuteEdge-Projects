import random
from faker import Faker

fake = Faker()

departments = ["IT", "HR", "Finance", "Sales", "Marketing", "Operations"]

with open("insert_1000.sql", "w") as f:
    f.write("INSERT INTO Employees (Name, DOB, PhoneNumber, Department, DateOfJoining) VALUES\n")
    
    values = []
    for i in range(1000):
        name = fake.name().replace("'", "''")  # escape single quotes
        dob = fake.date_of_birth(minimum_age=22, maximum_age=60).strftime('%Y-%m-%d')
        phone = fake.numerify('##########')  # 10-digit phone
        dept = random.choice(departments)
        doj = fake.date_between(start_date="-10y", end_date="today").strftime('%Y-%m-%d')
        
        values.append(f"('{name}', '{dob}', '{phone}', '{dept}', '{doj}')")
    
    f.write(",\n".join(values) + ";")
