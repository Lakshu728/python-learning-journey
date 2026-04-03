#Print numbers from 1 to 10 using a for loop.
# for i in range(1,11):
#     print("number",i)
    
    
#Print all even numbers from 1 to 20.
# for i in range(1,21):
#     if i%2==0:
#         print("even number ",i)
        
    

#Print all odd numbers from 1 to 20.
# for i in range(1,21):
#     if i%2!=0:
#         print("odd number ",i)   


#Print the multiplication table of 5.
# for i in range(1,11):
#     print("5","X",i,"=",5*i)


#Print the sum of numbers from 1 to 100.
# c=0
# for i in range (1,101):
#     c+=i
# print("the sum of numbers from 1 to 100 is ",c) 
  
  
  
#print each character of a string on a new line.
# word=input("enter any word: ")
# for char in word:
#     print(char)
        

#Count how many numbers are divisible by 3 between 1 and 50
# c=0
# for i in range(1,51):
#     if i%3==0:
#        c=c+1
# print("Total numbers divisible by 3 =", c)  


#factorial of a number
# num=int(input("Enter a number: "))
# f=1
# for i in range(1,num+1):
#     f=f*i
# print("The factorial of",num,"is",f)    

#reverse a number
# num=int(input("Enter a number: "))
# rev=0
# for i in range(num):
#     rev=rev*10+num%10
#     num=num//10
# print("The reverse of the number is",rev)   


#Print Fibonacci series up to n terms.
# n=int(input("Enter the number of terms: "))
# a=0
# b=1
# print("Fibonacci series up to",n,"terms:")
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c                 


#Find the sum of digits of a number.
# num=int(input("Enter a number: "))
# sum=0
# for i in range(num):
#     sum=sum+num%10
#     num=num//10
# print("The sum of digits of the number is",sum)     

             
#Check whether a number is prime or not.
# num=int(input("Enter a number: "))
# prime=True
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#             break  
# if prime:
#     print(num," is a prime number")
# else:
#     print(num," is not a prime number")             

#print all prime numbers between 1 and 100.
# for i in range(1,101):
#     prime=True
#     if i>1:
#      for j in range(2,i):
#        if i%j==0:
#            prime=False
#            break
#      if prime:
#         print(i)                    
     
     
#Count vowels in a string.
# text=input("enter any text: ")
# vowels="aeiouAEIOU"
# count=0
# for char in text:
#     if char in vowels:
#         count+=1
# print("number of vowels in the text is ",count)
         

#Print a list in reverse order using a loop.
# list1=[1,2,3,4,5,6] 
# for i in range(len(list1)-1,-1,-1):
#         print(list1[i])    
############
# for i in reversed(list1):
#     print(i)          

#print patterns using nested loops.
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print() 

# reverse pattern
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#number pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
    
 #reverse number pattern   
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()            


#piramid pattern
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()