import re
from save_all_contacts import save_all_contacts

def add_contact(all_contacts):

    while True:
            try:
                name = input("Enter name: ")
                if not name.strip():
                    raise ValueError("Name cannot be empty")
                if not any(char.isalpha() for char in name):
                    raise ValueError("Name must contain at least one letter")
                break
            except ValueError as e:
                print(f"Invalid input! {str(e)}")
                continue
    while True:
            try:
                number = int(input("Enter phone number: "))
                if number <= 0:
                    raise ValueError("Phone number must be a positive number")
                if any(contact["number"] == number for contact in all_contacts):
                    raise ValueError("Phone number is already saved")
                break
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("Invalid input! Please enter a numeric phone number.")
                else:
                    print(f"{e}")


    while True:
            email=input("Enter email: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                break
            else:
                print("Invalid email format! Please enter a valid email address.")
        
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
    print("Contact saved successfully!")


    return all_contacts


