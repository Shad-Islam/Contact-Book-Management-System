def save_all_contacts(all_contacts):
    with open("all_contacts.csv","w") as all_contacts_file:
        for contact in all_contacts:
            person=f"{contact["name"]},{contact["number"]},{contact["email"]},{contact["address"]},{contact["job_title"]}\n"
            all_contacts_file.write(person)
