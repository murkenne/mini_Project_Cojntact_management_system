'''
Mini Project: Contact Management System


Step 1: User Interface (UI):
Create a user-friendly command-line interface (CLI) for the Contact Management System.
Display a welcoming message and provide a menu with the following options:

Welcome to the Contact Management System! 
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file *BONUS*
8. Quit

Step 2: Contact Data Storage:
Use nested dictionaries as the main data structure for storing contact information.
Each contact should have a unique identifier 
(e.g., a phone number or email address) as the outer dictionary key.
Store contact details within the inner dictionary, including:
Name
Phone number
Email address
Additional information (e.g., address, notes).


'''


def read_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = {}
            for line in file:
                name, phone_number, email_address, notes = line.strip().split(',')
                # Use phone number (or email_address) as the key for the outer dictionary
                contacts[phone_number] = {
                    'name': name,
                    'phone number': phone_number,
                    'email address': email_address,
                    'notes': notes
                }
            return contacts
    except FileNotFoundError:
        return {}
    

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email_address = input("Enter the contact's email address: ")
    notes = input("Enter additional information (e.g., address, notes): ")
    
    if phone_number in contacts:
        print("This contact already exist.") 
    else:
        contacts[phone_number] = {
                    'name': name,
                    'phone number': phone_number,
                    'email address': email_address,
                    'notes': notes
                }
        print("Contact successfully added.")
    

def edit_contact(contacts):
    phone_number = input("Enter the contact's phone number: ")
    
    if phone_number in contacts:
        # Display current information
        print(f"Current name: {contacts[phone_number]['name']}")
        print(f"Current email: {contacts[phone_number]['email address']}")
        print(f"Current notes: {contacts[phone_number]['notes']}")

        # Ask for new information (skip if they press Enter)
        new_name = input("Enter new name (leave blank to keep current): ")
        new_email = input("Enter new email address (leave blank to keep current): ")
        new_notes = input("Enter new notes (leave blank to keep current): ")

        # Update only the fields where new input is provided
        if new_name:
            contacts[phone_number]['name'] = new_name
        if new_email:
            contacts[phone_number]['email address'] = new_email
        if new_notes:
            contacts[phone_number]['notes'] = new_notes
        
        print("Contact successfully updated.")
    else:
        print("Contact does not exist.")
  

def delete_contact(contacts):
    phone_number = input("Enter the phone number of the contact you want to delete: ")

    # Check if the contact exists
    if phone_number in contacts:
        # Confirm deletion
        confirmation = input(f"Are you sure you want to delete the contact for {contacts[phone_number]['name']}? (yes/no): ")
        if confirmation.lower() == 'yes':
            del contacts[phone_number]
            print("Contact successfully deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("Contact does not exist.")


def search_contacts(contacts):
    search_name = input("Enter the contact's name: ")
    
    found_contacts = []
    
    for contact_info in contacts.values():
        if (search_name.lower() in contact_info['name'].lower() or search_name == ""):
           found_contacts.append(contact_info)
           
    if not found_contacts:
        print("No contacts found.")
    else:
        print(f"Found {len(found_contacts)} contact(s):")
        for contact in found_contacts:
            print(contact)
        

def print_contact_details(name, phone_number, email_address, notes):
    print(f"Name: {name}, Phone Number: {phone_number}, Email Address: {email_address}, Notes: {notes}")
    
def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for phone_number, contact_info in contacts.items():
            # Use the helper function to print each contact's details
            print_contact_details(contact_info['name'], phone_number, contact_info['email address'], contact_info['notes'])

def import_contacts(contacts, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone_number, email_address, notes = line.strip().split(',')
                # Add the contact to the dictionary if it doesn't exist
                if phone_number not in contacts:
                    contacts[phone_number] = {
                        'name': name,
                        'phone number': phone_number,
                        'email address': email_address,
                        'notes': notes
                    }
            print("Contacts successfully imported.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def export_contacts(contacts, filename):
    try:
        with open(filename, 'w') as file:
            for phone_number, contact_info in contacts.items():
                line = f"{contact_info['name']},{phone_number},{contact_info['email address']},{contact_info['notes']}\n"
                file.write(line)
        print(f"Contacts successfully exported to {filename}.")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

def main():
    contacts = read_contacts('contact_storage.txt')
    
    try:
        # Run the command-line contact management application
        while True:
            print("Welcome to the Contact Management System!\nMenu:")
            print("1. Add a new contact")
            print("2. Edit an existing contact")
            print("3. Delete a contact")
            print("4. Search for a contact")
            print("5. Display all contacts")
            print("6. Import contacts from a text file")
            print("7. Export contacts to a text file")
            print("8. Quit")
            
            choice = input("Enter your choice: ")
            if choice == '1':
                add_contact(contacts)
            elif choice == '2':
                edit_contact(contacts)
            elif choice == '3':
                delete_contact(contacts)
            elif choice == '4':
                search_contacts(contacts)
            elif choice == '5':
                display_contacts(contacts)
            elif choice == '6':
                filename = input("Enter the filename to import contacts from: ")
                import_contacts(contacts, filename)
            elif choice == '7':
                filename = input("Enter the filename to export contacts to: ")
                export_contacts(contacts, filename)
            elif choice == '8':
                print("Thank you for using the Contact Management System.")
                break
            else:
                print("Invalid choice. Please try again.")
                
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")
    except ValueError:
        print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
