# enter student name
name=input("Enter student name:")
# enter student marks
sub1=int(input("enter marks of subject 1:"))
sub2=int(input("enter marks of subject 2:"))
sub3=int(input("eenter marks of subject 3:"))
print("The marks of subect 1 is ", sub1)
print("The marks of subect 2 is ", sub2)
print("The marks of subect 3 is ", sub3)
# calculate total marks
total=sub1+sub2+sub3
percentage=total/300*100
print("the total percentage of student ", name ," is ", percentage,"%")

