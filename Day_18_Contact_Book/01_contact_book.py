# Contact Book – Version 01 (Improved & Commented)
# Author: Faiz ur Rehman Ashrafi
# Week 3 – File Handling & Functions
# Purpose: Manage contacts (view, add, delete) with file storage


def load_contact(filename):
    """Load contacts from file or create an empty list if file not found."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            contacts = [contact.strip() for contact in f.readlines()]
    except FileNotFoundError:
        print(f"{filename} file not found. Starting with empty contact list.\n")
        contacts = []
    return contacts


def save_contact(filename, contacts):
    """Save all contacts back to the file."""
    with open(filename, "w", encoding="utf-8") as f:
        for contact in contacts:
            f.write(f"{contact}\n")


def show_contacts(contacts):
    """Display all contacts with numbering."""
    if not contacts:
        print("Contact list is empty.\n")
    else:
        print("\nYour Contact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact}")
        print()  # Blank line for spacing


def add_contact(filename, contacts):
    """Add a new contact and save it to file."""
    new_contact_name = input("Enter Name: ").strip()
    new_contact_phone = input("Enter Phone#: ").strip()

    if not new_contact_name or not new_contact_phone:
        print("Empty contact not allowed.\n")
        return

    # Optional: prevent duplicate contact names
    for contact in contacts:
        if new_contact_name.lower() in contact.lower():
            print(f"Contact with name '{new_contact_name}' already exists.\n")
            return

    new_contact = f"Name: {new_contact_name} | Phone#: {new_contact_phone}"
    contacts.append(new_contact)
    save_contact(filename, contacts)
    print(f"New Contact Added: {new_contact}\n")


def delete_contact(filename, contacts):
    """Delete a contact by serial number."""
    if not contacts:
        print("No contacts to delete.\n")
        return

    show_contacts(contacts)

    try:
        num = int(input("Enter Contact S# to delete: "))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            save_contact(filename, contacts)
            print(f"Contact Removed: {removed}\n")
        else:
            print("Invalid Contact S#.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    """Main program loop for Contact Book."""
    filename = "contacts.txt"
    contacts = load_contact(filename)

    while True:
        print("======= CONTACT BOOK MENU =======")
        print("1. Show Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Exit")
        print("===================================")

        choice = input("Enter choice (1–4): ").strip()

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(filename, contacts)
        elif choice == "3":
            delete_contact(filename, contacts)
        elif choice == "4":
            print("Exiting... Contacts saved successfully. See you again!\n")
            break
        else:
            print("Invalid Choice! Please enter between 1–4.\n")


if __name__ == "__main__":
    main()
