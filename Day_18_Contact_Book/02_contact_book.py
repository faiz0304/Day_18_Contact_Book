# Contact Book – Version 02 (Improved)
# Week 3: File Handling & Functions
# Author: Faiz ur Rehman Ashrafi
# Features: Add, View, Search, Delete, Save contacts in file

FILENAME = "contacts.txt"


def add_contact(name, phone):
    """Add a new contact to the file (prevents duplicates)."""
    # Prevent adding duplicate contact names
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            existing = f.read().lower()
            if name.lower() in existing:
                print(f"Contact '{name}' already exists. Try another name.\n")
                return
    except FileNotFoundError:
        pass  # No file yet, so continue to create new one

    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"{name},{phone}\n")
    print(f"Contact saved successfully: {name} - {phone}\n")


def view_contacts():
    """Display all saved contacts."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            contacts = [line.strip() for line in f.readlines()]
            if not contacts:
                print("No contacts found.\n")
                return
            print("\nContact List:")
            for contact in contacts:
                # Safe split (avoid crash if malformed line)
                parts = contact.split(",")
                if len(parts) == 2:
                    name, phone = parts
                    print(f"👤 {name} - {phone}")
            print()  # Extra spacing
    except FileNotFoundError:
        print("No contact file found. Add a contact first!\n")


def search_contact(search_name):
    """Search for a contact by name."""
    found = False
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    continue
                name, phone = parts
                if name.lower() == search_name.lower():
                    print(f"🔍 Found: {name} - {phone}\n")
                    found = True
                    break
        if not found:
            print(f"No contact found with name '{search_name}'.\n")
    except FileNotFoundError:
        print("Contact file not found!\n")


def delete_contact(del_name):
    """Delete a contact by name."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            contacts = [line.strip() for line in f.readlines()]

        deleted = False
        with open(FILENAME, "w", encoding="utf-8") as f:
            for contact in contacts:
                parts = contact.split(",")
                if len(parts) != 2:
                    continue
                name, phone = parts
                if name.lower() != del_name.lower():
                    f.write(f"{name},{phone}\n")
                else:
                    deleted = True

        if deleted:
            print(f"Contact '{del_name}' deleted successfully.\n")
        else:
            print(f"No contact found with name '{del_name}'.\n")
    except FileNotFoundError:
        print("Contact file not found!\n")


# ---------- Main Menu ----------
while True:
    print("===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("===============================")

    choice = input("Enter your choice (1–5): ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        add_contact(name, phone)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_name = input("Enter name to search: ").strip()
        search_contact(search_name)

    elif choice == "4":
        del_name = input("Enter name to delete: ").strip()
        delete_contact(del_name)

    elif choice == "5":
        print("Exiting Contact Book. Goodbye!\n")
        break

    else:
        print("Invalid choice. Please select between 1–5.\n")
