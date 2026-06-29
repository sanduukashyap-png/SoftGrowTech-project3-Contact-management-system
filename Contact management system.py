contacts = {}

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    # Display Contacts
    elif choice == "2":
        if contacts:
            print("\nContact List:")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")
        else:
            print("No contacts found.")

    # Search Contact
    elif choice == "3":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"Phone Number: {contacts[search_name]}")
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")1
        