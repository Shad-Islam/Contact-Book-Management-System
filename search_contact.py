def  search_contact(all_contacts):
    result=[]
    query = input("Enter the search query: ")
    for contact in all_contacts:

        is_number_match = query.isdigit() and int(query) == contact["number"]
        if query.lower() in contact['name'].lower() or is_number_match:
            result.append(contact)
    if result:
        print("Search result: ")
        for i,contact in enumerate(result,1) :
            print(f"{i} name: {contact["name"]},number: {contact["number"]},email: {contact["email"]},address: {contact["address"]},job title: {contact["job_title"]} ")
    else:
        print("No result found")