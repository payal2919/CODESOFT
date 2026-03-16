#contact book program
contacts = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contacts.append({"name": name, "phone": phone, "email":email, "address":address})

        print("Contact added successfully")

    elif choice == "2":
        if contacts == []:
            print("No contacts saved")
        else:
            print("\nSaved Contacts:")
            for contact in contacts:
                print(contact["name"],"-",contact["phone"])

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search.lower():
                print("\nContact Found")
                print("Name: ",contact["name"])
                print("Phone: ", contact["phone"])
                print("Email:",contact["email"])
                print("Address:",contact["address"])
                found = True

        if found == False:
                print("Contact not found")
                

    elif choice == "4":
        n = input("Enter name to update: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == n.lower():
                contact["phone"] = input("Enter new phone: ")
                contact["email"] = input("Enter new email: ")
                contact["address"] = input("Enter new address: ")
                print("Contact updated")
                found = True

        if found == False:
                print("Contact not found")

    elif choice == "5":
        n = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == n.lower():
                contacts.remove(contact)
                print("Contact deleted")
                found = True
                break

        if found == False:
                print("Contact not found")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.Try again!")

