import json
import add_contact
import delete_contact
import view_all_contact

try:
    with open("all_contacts.json","r") as file:
        all_contacts = json.load(file)
except FileNotFoundError:
    all_contacts = []

while True:
    print("\nWelcome to library management system \n")
    print("Press 0 for exit")
    print("Press 1 for add contact")
    print("Press 2 for delete contact")
    print("press 3 for view all contacts")

    menu = input("Please select a number: ")
    print("\n")

    if menu == "0":
        print("Thank you for using contact book management system")
        break
    elif menu == "1":
        all_contacts=add_contact.add_contact(all_contacts)
    elif menu == "2":
        delete_contact.delete_contact(all_contacts)
    elif menu == "3":
        view_all_contact.view_all_contact()
    else:
        print("Invalid input")
