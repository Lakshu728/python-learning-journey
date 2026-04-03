# Python 3.10 introduced the match-case statement, which is a more powerful
# and flexible way to handle multiple conditions compared to traditional if-elif-else statements. 
# It allows you to match patterns against values and execute code based on those patterns.

#weekday using match case
# day=int(input("ENTER THE DAY: "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("sunday") 
#     case _:
#         print("Invalid day")
        
        
#calculator using match case
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: ")) 
operator=input("enter operator (+, -, *, /, %): ")
match operator:
    case "+":
        print(num1," + ",num2," = ",num1+num2)
    case "-":
        print(num1," - ",num2," = ",num1-num2)   
    case "*":
         print(num1," * ",num2," = ",num1*num2)
    case "/":
        if num2!=0:
             print(num1," / ",num2," = ",num1/num2) 
        else:
                print("Cannot divide by zero")
    case "%":
        if num2!=0:
             print(num1," % ",num2," = ",num1%num2)       
        else:
                print("Cannot divide by zero")  
    case _:
        print("Invalid operator")                  
        
                           