from save_all_contacts import save_all_contacts

def delete_contact(all_contacts):
    index = int(input("Enter the contact index number: "))
    if 1 <= index <= len(all_contacts):
        contact =all_contacts[index-1]
        del all_contacts[index-1]
        save_all_contacts(all_contacts)
        print(f"\nindex number {index} contact is deleted")
    else:
        print("\nInvalid index number. Please enter a valid index.")
