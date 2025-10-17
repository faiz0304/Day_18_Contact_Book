# Contact Saver (Improved Version of 01.py)
# This script takes a name and phone number from user
# and stores them in a text file, preserving previous data.

# Take input from user
name = input("Enter Name: ")
phone = input("Enter Phone: ")

# File to store contacts
filename = "contacts.txt"

# Open file in append mode so previous data is not erased
with open(filename, "a", encoding="utf-8") as f:
    # Write contact info with newline for separation
    f.write(f"Name: {name} | Phone: {phone}\n")
print("Contact saved successfully!")

# Display all saved contacts
print("\nCurrent Contact List:")
with open(filename, "r", encoding="utf-8") as f:
    contact = f.read()
    print(contact if contact else "No contacts found yet.")
