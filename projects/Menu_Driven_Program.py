number = []
while True:
    print("\n-------Menu-------")
    print("1. Add Element")
    print("2. Display List")
    print("3. Remove Element")
    print("4. Search Element")
    print("5. sort Element")
    print("6. Clear List")
    print("7. Exit")
    
    choice=int(input("Enter your choice: "))
    
    match choice:
        case 1 :
            n = int(input("How many elements you want to add: "))
            for i in range(n):
                num = int(input(f"Enter number {i+1}: "))
                number.append(num)
            print("Elements added.")
            
        case 2 :
            print("List = ",number)
            
        case 3 :
            num=int(input("Enter number to remove: "))
            if num in number:
                 number.remove(num)
                 print("Element removed.")  
            else:
                 print("Element not found.")
                 
        case 4 :
            num = int(input("Enter number to search: "))
            if num in number:
                print("Element found at index:", number.index(num))
            else:
                print("Element not found.")  
                
        case 5 :
            number.sort()     
            print("List sorted.",number)   
            
        case 6:  
            number.clear()  
            print("List cleared.")

        case 7:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Try again.")         
                       