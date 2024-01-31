# Script 2: read_guests.py

import csv

# Open the CSV file for reading
with open('guests.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row

    guests = {}
    tables = {i: 10 for i in range(1, 11)}  # assuming 10 tables with 10 seats each
    for row in reader:
        first_name, last_name, table_number, seat_number, family_members = row
        family_members = family_members.split(", ") if family_members else []
        guests[(first_name.lower(), last_name.lower())] = (table_number, seat_number, family_members)
        for member in family_members:
            guests[(member.lower(), "")] = (table_number, seat_number, [])

    while True:
        first_name = input("Enter a guest's first name or 'quit' to stop: ").lower()
        if first_name == 'quit':
            break
        last_name = input("Enter the guest's last name: ").lower()
        if (first_name, last_name) in guests:
            table_number, seat_number, family_members = guests[(first_name, last_name)]
            print(f"{first_name} {last_name} will be seated at table {table_number}, seat number {seat_number}")
            for member in family_members:
                member_table, member_seat, _ = guests[(member.lower(), "")]
                print(f"Family member {member} will be seated at table {member_table}, seat number {member_seat}")
        else:
            print("Guest not found.")
    
    