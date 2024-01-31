# Script 1: register_guests.py

import csv
import os

# Open the CSV file for appending
with open('guests.csv', 'a', newline='') as file:
    writer = csv.writer(file)

    # Write the header only if the file is empty
    if os.stat('guests.csv').st_size == 0:
        writer.writerow(["First Name", "Last Name", "Table Number", "Seat Number", "Family Members"])

    # Update tables dictionary to reflect the number of seats at each table
    tables = {i: 10 for i in range(1, 7)}
    tables.update({i: 8 for i in range(7, 15)})
    tables.update({i: 7 for i in range(15, 21)})
    guests = set()

    while True:
        first_name = input("Enter guest's first name or 'quit' to stop: ").lower()
        if first_name == 'quit':
            break
        last_name = input("Enter guest's last name: ").lower()
        if (first_name, last_name) in guests:
            print("Guest already exists. Skipping.")
            continue
        guests.add((first_name, last_name))
        status = input("Is the guest single or family? ").lower()
        family_members = []
        family_size = 1  # count the guest themselves
        if status == 'family':
            spouse_name = input("Enter spouse's name: ").strip()
            kids_names = input("Enter kids' names (separated by comma): ").split(',')
            kids_names = [name.strip() for name in kids_names if name.strip()]
            family_members = [name for name in [spouse_name] + kids_names if name]
            family_size += len(family_members)  # count the spouse and each kid
        table_number = int(input("Enter table number: "))
        if tables[table_number] < family_size:
            print("Not enough available seats at this table. Please choose another table.")
            continue
        seat_number = tables[table_number] - family_size + 1
        writer.writerow([first_name, last_name, table_number, seat_number, ", ".join(family_members)])
        for member in family_members:
            seat_number += 1
            writer.writerow([member, "", table_number, seat_number, ""])
        tables[table_number] -= family_size

        # Ask if the user wants to see how many seats are left
        if input("Do you want to know how many seats are left? (yes/no) ").lower() == 'yes':
            print("Remaining seats:")
            for table, seats in tables.items():
                print(f"There are {seats} seats left on table {table}.")