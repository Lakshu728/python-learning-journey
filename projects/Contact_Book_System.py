contacts=[]
def add_contact():
    '''add a new contact with name, contact, email.'''
    name =  input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter email: ").strip()
    
    # Duplicate check
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("Contact already exists!")
            return
    contacts.append((name, phone, email))
    print("Contact added successfully!")
    
    #view contact
def view_contact():
     '''display all contact'''
     if not contacts:
            print("No contact found.")
            return
     print("\n contact list:")
     for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact[0]},Phone: {contact[1]}, Email: {contact[2]}")
    
    
    #search contact
def search_contact():
    '''search contact by name (partial search)'''
    keyword = input("Enter name to search: ").strip().lower()
        
    found = False
    for contact in contacts:
            if keyword in contact[0].lower():
                print(f"Found : {contact[0]}, {contact[1]}, {contact[2]}")
                found = True
    if not found:
        print("contact not found")
    
    #update contact
def update_contact():
    '''Update exsiting contact details'''
    name = input("Enter name to update : ").strip().lower()
        
    for i, contact in enumerate(contacts):
            if contact[0].lower() == name:
                print("Enter new details : ")
                new_name = input("Enter new name: ").strip()
                new_phone = input("Enter new phone: ").strip()
                new_email = input("Enter new email: ").strip()
                
                contacts[i]= (new_name, new_phone, new_email)
                print("contact updated! ")
                return
    print (" contact not found!!!")
    
    
    #delete contact details
def delete_contact():
    ''' Delete contact'''
    name = input("Enter name to delete: ").strip().lower()
        
    for contact in contacts:
        if contact[0].lower() == name:
            contacts.remove(contact)
            print("Contact deleted!")
            return
    print (" contact not found!!!")
    
       
    #count contacts
def count_contacts():
        '''count contacts'''
        print(f"total contacts: {len(contacts)}")     
        
      #sort contacts     
def sort_contact():
        '''sort contact alphabetically'''
        contacts.sort(key=lambda x: x[0].lower())
        print("contacts sorted successfully! ")
        
       
#main menu
while True:
    print("\n ======= smart contact book ======")    
    print("1. Add contact")  
    print("2. View contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Count contact")
    print("7. Sort contact")
    print("8. Exit")
   
   
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! please enter number only")
        continue
    
    match choice:
        
        case 1 :
            add_contact()
            
        case 2 :
            view_contact()
            
        case 3 :
            search_contact() 
            
        case 4 :
            update_contact()
            
        case 5 :
            delete_contact()
            
        case 6 :                  
            count_contacts() 
            
        case 7 :
            sort_contact()
            
        case 8 :
            print("Exiting Program")
            break
        
        case _:
            print("Invalid choice")          
           
            