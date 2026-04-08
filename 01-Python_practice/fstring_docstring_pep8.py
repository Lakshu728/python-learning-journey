# fstring, docstring and pep 8 in one program

def calculate_result(name, marks):
    ''' this function take student name and student marks,
    and prints the result using f-string.
    It also checks pass or fail condition.
    '''
    if marks>= 40:
        result = "pass"
    else:
        result = "fail"
        
    print("-----result-----")    
    print(f"student name : {name}")
    print(f"Marks: {marks}")
    print(f"Result: {result}")        
    
# Taking input from user
student_name = input("Enter student name: ")
student_marks = float(input("Enter marks: "))

#calling function
calculate_result(student_name, student_marks)   