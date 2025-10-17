# Contact Saver – Version 02 (Improved)
# Stores multiple contacts (Name & Phone) and saves them in a file

names = []
phones = []

print("Enter contact details (type 'q' to stop):")
while True:
    name = input("Name: ")
    if name.lower() == "q":
        break
    phone = input("Phone #: ")
    names.append(name)
    phones.append(phone)

filename = "contacts.txt"

# Combine name and phone using zip() → list of tuples
contacts = list(zip(names, phones))

# Use append mode to keep old data
with open(filename, "a", encoding="utf-8") as f:
    for name, phone in contacts:
        f.write(f"Name: {name}, Phone#: {phone}\n")

print("\nContacts saved successfully!")

# Display all contacts from file
print("\nContact List:")
try:
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
        if lines:
            for i, item in enumerate(lines, start=1):
                print(f"{i}. {item}")
        else:
            print("No contacts found.")
except FileNotFoundError:
    print("Contact file not found.")
