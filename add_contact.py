from save_all_contacts import save_all_contacts

def add_contact(all_contacts):
    name=input("Enter name: ")
    number=int(input("Enter phone number: "))
    email=input("Enter email: ")
    address= input("Enter address: ")
    job_title= input("Enter job title: ")

    contact = {
        "name":name,
        "number":number,
        "email":email,
        "address":address,
        "job_title":job_title,
    }

    all_contacts.append(contact)
    save_all_contacts(all_contacts)

    print("Contact create successfully")

    return all_contacts


