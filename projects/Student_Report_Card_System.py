# Student Report Card System

while True:
    student_name = input("\nEnter student name: ")

    total_marks = 0
    subjects = {}   # dictionary to store subject and marks

    # loop for 5 subjects
    for i in range(1, 6):
        subject = input(f"Enter subject {i} name: ")

        marks = float(input(f"Enter marks obtained in {subject}: "))

        # validation
        if marks < 0 or marks > 100:
            print("Invalid marks! Please enter between 0 to 100.")
            continue

        subjects[subject] = marks   # store subject and marks
        total_marks += marks

    # calculate percentage
    percentage = (total_marks / 500) * 100

    # determine grade
    if percentage >= 90:
        grade = 'A+'
        remark = "Excellent"
    elif percentage >= 80:
        grade = 'A'
        remark = "Very Good"
    elif percentage >= 70:
        grade = 'B'
        remark = "Good"
    elif percentage >= 60:
        grade = 'C'
        remark = "Average"
    elif percentage >= 50:
        grade = 'D'
        remark = "Needs Improvement"
    else:
        grade = 'E'
        remark = "Fail"

    # print report card
    print("\n----- Report Card -----")
    print(f"Student Name: {student_name}")

    print("\nSubjects and Marks:")
    for sub, mark in subjects.items():
        print(f"{sub} : {mark}")

    print(f"\nTotal Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Remark: {remark}")

    # repeat or exit
    choice = input("\nDo you want to enter another student? (yes/no): ").lower()

    if choice == 'no':
        print("Program Ended.")
        break