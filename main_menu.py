import add_contact
import view_all_contact
all_contacts = []

while True:
    print("Welcome to library management system")
    print("Press 0 for exit")
    print("Press 1 for add contact")
    print("Press 2 for delete contact")
    print("press 3 for view all contacts")

    menu = input("Please select a number: ")

    if menu == "0":
        print("Thank you for using contact book management system")
        break
    elif menu == "1":
        all_contacts=add_contact.add_contact(all_contacts)
    elif menu == "2":
        print("select 2")
    elif menu == "3":
        view_all_contact.view_all_contact(all_contacts)
    else:
        print("Invalid input")
