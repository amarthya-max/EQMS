import datetime
PRODUCT_FILE = 'products.txt'
SOURCE_FILE = 'source.txt'
ENQUIRY_FILE = 'enquiries.txt'

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = [eval(line) for line in file.read().splitlines()]
        return data if data else []
    except FileNotFoundError:
        return []
    
def save_data(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

def add_product():
    product_name = input("Enter product name: ")
    product_code = input("Enter product code: ")
    description = input("Enter the product description: ")
    price = input("Enter the product price: ")
    
    products.append({
        'id':  len(products) +1,
        'name': product_name,
        'code': product_code,
        'description': description,
        'price' : price 
     })
    print(f"Product '{product_name}' added successfully") 

# add_source 
    #input: source_name
    # wite code below 
def add_source():
    source_name = input("Enter the source name: ")
    sources.append({
        'id' : len(sources) + 1,
        'name': source_name
    })
    print(f"Source '{source_name}' added successfully.")


# register_enquiry

def register_enquiry():
    customer_name = input("Enter customer name: ")
    contact_person_name = input("Enter contact person name: ")
    address = input("Enter address: ")
    telephone = input("Enter telephone number: ")
    source_name = input("Enter the source for the enquiry: ")
    email_id = input("Enter email id: ")
    remark = input("Enter remark: ")

    enquiries.append({
        'id' : len(enquiries) + 1,
        'date' : str(datetime.date.today()),
        'customer_name': customer_name,
        'contact_person_name': contact_person_name,
        'address': address,
        'telephone': telephone,
        'source name': source_name,
        'email_id' : email_id,
        'remark' : remark

    })
    print("Enquiry registered successfully.")



# view enquiries
    
def view_enquiries():
    print("\n===Enquiries===")
    for enquiry in enquiries:
        print(enquiry)
    
# delete_enquires()
def delete_enquiry():
    view_enquiries()
    if not enquiries:
        print("No enquires to delete.")
        return
    try:
        index_to_delete = int(input("Enter the number of the enquiry to delete: ")) -1
        if 0 <= index_to_delete <len(enquiries):
            delete_enquiry = enquiries.pop(index_to_delete)
            print(f"Enquiry {index_to_delete + 1} deleted: {delete_enquiry}")
        else:
            print("Invalid index. No enquiries deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")




def main_menu():

    while True:
        print("\n=== Main Menu ===")
        print("1. Add Product")
        print("2. Add Source")
        print("3. Register Enquiry")
        print("4. View Enquiry")
        print("5. Delete Enquiry")
        print("6. Exit")

       
        

        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            add_source()
        elif choice == '3':
            register_enquiry()
        elif choice == '4':
            view_enquiries()
        elif choice == '5' :
            delete_enquiry()
        elif choice == '6':
            print("Exiting the EQMS")
            break;
        else:
            print("Invalid choice. Please select from the above options")




if __name__ == "__main__":
    products = load_data(PRODUCT_FILE)
    sources = load_data(SOURCE_FILE)
    enquiries = load_data(ENQUIRY_FILE)

    main_menu()

    save_data(products, PRODUCT_FILE)
    save_data(sources, SOURCE_FILE)
    save_data(enquiries, ENQUIRY_FILE)