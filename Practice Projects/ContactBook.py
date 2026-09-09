contacts = {}

while True:
    print("\nCONTACT BOOK\n")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit Contact")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("\nEnter name: ")

        if name in contacts:
            print(f"Contact name {name} already exists!")

        else:
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")

            contacts[name] = {
                'age': age,
                'email': email,
                'mobile': mobile
            }

            print(f"Contact name {name} has been created successfully!")

    elif choice == 2:
        name = input("Enter contact name to view: ")

        if name in contacts:
            contact = contacts[name]

            print(f"\nName: {name}")
            print(f"Age: {contact['age']}")
            print(f"Mobile Number: {contact['mobile']}")
            print(f"Email ID: {contact['email']}")

        else:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter name you want to update: ")

        if name in contacts:
            age = int(input("Enter updated age: "))
            email = input("Enter updated email id: ")
            mobile = input("Enter updated mobile number: ")

            contacts[name] = {
                'age': age,
                'email': email,
                'mobile': mobile
            }

            print(f"Contact name {name} has been updated successfully!")

        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter name you want to delete: ")

        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully!")

        else:
            print("Contact not found!")

    elif choice == 5:
        search_name = input("Enter contact name to search: ")

        found = False

        for name, contact in contacts.items():

            if search_name.lower() in name.lower():

                print(f"\nFound Contact:")
                print(f"Name: {name}")
                print(f"Age: {contact['age']}")
                print(f"Mobile Number: {contact['mobile']}")
                print(f"Email ID: {contact['email']}")

                found = True

        if not found:
            print(f"No contact found with name {search_name}")

    elif choice == 6:
        print(f"Total number of contacts in your book: {len(contacts)}")

    elif choice == 7:
        print("Closing Program..")
        break

    else:
        print("Invalid Inputs!")