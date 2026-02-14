def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    nam = input()
    if nam in contact_book.keys():
        print("Contact already exists!")
    else:
        contact_book[nam] = {}
        contact_book[nam]["phone"] = input()
        contact_book[nam]["email"] = input()
        contact_book[nam]["address"] = input()
        print("Contact added successfully!")

def view_contact(contact_book):
    nam = input()
    if nam in contact_book.keys():
        print("Name:",nam)
        print("Phone:",contact_book[nam]["phone"])
        print("Email:",contact_book[nam]["email"])
        print("Address:",contact_book[nam]["address"])
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    nam = input()
    if nam in contact_book.keys():
        contact_book[nam]["phone"] = input()
        contact_book[nam]["email"] = input()
        contact_book[nam]["address"] = input()
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    nam = input()
    if nam in contact_book.keys():
        del contact_book[nam] 
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if len(contact_book) == 0:
        print("No contacts available.")
    for nam in contact_book.keys():
        print("Name:",nam)
        print("Phone:",contact_book[nam]["phone"])
        print("Email:",contact_book[nam]["email"])
        print("Address:",contact_book[nam]["address"])
        print("")
    
   

contact_book = {}
i = 0
while i == 0:
    display_menu() 
    status = int(input())
    match status:
        case 1:
            add_contact(contact_book)
        case 2:
            view_contact(contact_book)
        case 3:
            edit_contact(contact_book)
        case 4:
            delete_contact(contact_book)
        case 5:
            list_all_contacts(contact_book)
        case 6:
            i += 1
        case _:
            print("wrong code")
