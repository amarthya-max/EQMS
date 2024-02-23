PRODUCT_FILE = 'products.txt'
SOURCE_FILE = 'source.txt'
ENQUIRY_FILE = 'enquiries.txt'

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = eval(file.read())
        return data if data else []
    except FileNotFoundError:
        return []
    
def save_data(data, filename):
    with open(filename, 'w') as file:
        file.write(repr(data))

def add_product(data, filename):
    product_name = input("Enter product name")
    products.append({"id: len(products)+1" "name": product_name})
    print(f"Product '{product_name}' added successfully.")

# add_source 
    #input: source_name
    # wite code below 



# register_enquiry(
    #input: product_name, source_name


# view enquiries
    #print
    

# delete_enquires()
    #view_enquires()
    #check fr enquiry , then print No enquies to delete
    #delete 




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
            register_enquriy()
        elif choice == '4':
            view_enquiries()
        elif choice == '5' :
            delete_enquiries()
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