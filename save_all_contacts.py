import json
def save_all_contacts(all_contacts):
    with open("all_contacts.json","w") as file:
        json.dump(all_contacts, file, indent=4)
        print("Contact saved successfully!")