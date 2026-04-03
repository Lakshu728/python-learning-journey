#Print numbers from 1 to 20 using while loop
# i=1
# while i<=20:
#     print("number", i)
#     i=i+1

#Print all even numbers from 1 to 20 using while loop
# i=1
# while i<=20:
#      if i%2==0:
#          print("even number ",i)
#          i=i+1
#      else:
#          i=i+1
             
#print all odd numbers from 1 to 20 using while loop
# i=1
# while i<=20:
#     if i%2!=0:
#         print("odd number ",i)
#         i=i+1
#     else:
#         i=i+1


#Print the multiplication table of 5 using while loop
# num=int(input("enter a number: "))
# i=1
# while i<=10:
#     print(num,"X",i,"=",num*i)
#     i=i+1 


#Print the sum of numbers from 1 to 50 using while loop
# i=1
# c=0
# while i<=50:
#     c=c+i
#     i=i+1
# print("the sum of numbers from 1 to 50 is ",c) 
    
#Print each character of a string on a new line using while loop
# word=input("enter any word: ")
# i=0
# while i<len(word):
#     print(word[i])
#     i=i+1

#count how many numbers are divisible by 3 between 1 and 50 using while loop
# i=1
# c=0
# while i<=50:
#     if i%3==0:
#         c=c+1
#         i=i+1
#     else:    
#         i=i+1
# print("Total numbers divisible by 3 =", c)
        
#factorial of a number using while loop
# num=int(input("enter a number: "))
# f=1
# i=1
# while i<=num:
#     f=f*i
#     i=i+1
# print("the factorial of ",num,"is",f)
        
#reverse a number using while loop
# num=int(input("enter a number: "))
# rev=0
# while num>0:
#     rev=rev*10+num%10
#     num=num//10
# print("the reverse of the number is",rev)   

#Print the Fibonacci sequence up to a certain number using while loop
# num=int(input("enter a number: "))
# a=0
# b=1
# print("Fibonacci series up to",num,"terms:")
# while a<=num:
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c
    
#Find the sum of digits of a number using while loop
# num=int(input("enter a number: "))
# sum=0
# while num>0:
#     sum=sum+num%10
#     num=num//10
# print("the sum of digits of the number is",sum)        


#number in palindrome or not using while loop
num=int(input("enter a number: "))
rev=0
temp=num
while temp>0:
    rev=rev*10+temp%10
    temp=temp//10
if num==rev:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")                 