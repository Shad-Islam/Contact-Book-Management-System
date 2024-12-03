import json
def view_all_contact():
    with open("all_contacts.json","r") as file:
        contacts = json.load(file)
        if contacts:
            for index, contact in enumerate(contacts, 1):
                print(f"Contact #{index}")
                print(f"Name: {contact['name']}")
                print(f"Number: {contact['number']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                print(f"Job Title: {contact['job_title']}")
                print("-" * 30)
                # print("\n")
        else:
            print("No contacts found")


