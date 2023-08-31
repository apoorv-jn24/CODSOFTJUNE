contacts = {}


def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added.")


def view_contact(name):
    if name in contacts:
        print(f"Name: {name}\nPhone: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")


def update_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print(f"Contact '{name}' updated.")
    else:
        print(f"Contact '{name}' not found.")


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")


while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Select an option (1/2/3/4/5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        name = input("Enter name: ")
        view_contact(name)
    elif choice == '3':
        name = input("Enter name: ")
        new_phone = input("Enter new phone number: ")
        update_contact(name, new_phone)
    elif choice == '4':
        name = input("Enter name: ")
        delete_contact(name)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
