import os

# Function to load contacts from file
def load_contacts(file_name):
    contacts = {}
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts[name] = {'Phone': phone, 'Email': email}
    return contacts

# Function to save contacts to file
def save_contacts(file_name, contacts):
    with open(file_name, 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['Phone']},{info['Email']}\n")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {'Phone': phone, 'Email': email}
        print(f"Contact for {name} added successfully.")

# Function to search contact by name
def search_contact(contacts):
    name = input("Enter Name to Search: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print(f"No contact found for {name}.")

# Function to update contact information
def update_contact(contacts):
    name = input("Enter Name to Update: ")
    if name in contacts:
        phone = input("Enter new Phone: ")
        email = input("Enter new Email: ")
        contacts[name] = {'Phone': phone, 'Email': email}
        print(f"Contact for {name} updated successfully.")
    else:
        print(f"No contact found for {name}.")

# Main Program
def main():
    file_name = 'contacts.txt'
    contacts = load_contacts(file_name)

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            save_contacts(file_name, contacts)
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == '__main__':
    main()
