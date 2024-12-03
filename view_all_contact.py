def view_all_contact(all_contacts):
    if all_contacts != []:
         for contact in all_contacts:
            print(f"name: {contact["name"]},number: {contact["number"]},email: {contact["email"]},address: {contact["address"]},job title: {contact["job_title"]}")
    else:
        print("No contact found")


