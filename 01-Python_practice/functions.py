# arithmetic operations using function
# def add(a,b):
#     c=a+b
#     return c
# def sub(a,b):
#     c=a-b
#     return c
# def mul(a,b):
#     c=a*b
#     return c
# def div(a,b):
#     c=a/b
#     return c
# def mod(a,b):
#     c=a%b
#     return c
# def avg(a,b):
#     c=(a+b)/2
#     return c
# a=int(input("enter 1st number: "))
# b=int(input("enter 2nd value: "))
# c=add(a,b)
# print("sum of ",a," and ",b," is ",c)
# d=sub(a,b)
# print("difference of ",a," and ",b," is ",d)
# e=mul(a,b)
# print("product of ",a,"and ",b," is",e)
# f=div(a,b)
# print("division of ",a," and ",b," is ",f)      
# g=mod(a,b)
# print("modulus of ",a," and ",b," is ",g)
# h=avg(a,b)
# print("average of ",a," and ",b," is ",h)

#less or greater 
# def compare(a,b):
#     if a>b:
#         print(a,"greater than ",b)
#     elif a<b:
#         print(a,"greater than ",b)
#     else:
#         print(a," and ",b," are equal")
        
# a=int(input("enter 1st number: "))
# b=int(input("enter 2nd number: "))
# compare(a,b)
        
# square of a number
# def square(a):
#     print("square of ",a,"is",a*a)
    
# def cube(a):
#     print("cube of ",a,"is",a*a*a)
    
# a=int(input("enter a number: "))
# square(a)
# cube(a)

# factorial of a number
# def fac(a):
#     f=1
#     for i in range(1, a+1):
#         f=f*i
#     print("factorial of ",a," is ",f)
    
# a=int(input("enter a number: "))
# fac(a)


# fibonacci series
# def fib(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a,end=" ")
#         c=a+b
#         a=b
#         b=c
        
# n=int(input("enter the number of terms: "))
# fib(n)
 

#palindrome
# def palindrome(s):
#     if s==s[::-1]:
#         print(s," is a palindrome")
#     else:
#         print(s," is not a palindrome") 
        
# s=input("enter a string:")
# palindrome(s)    


#largest of three numbers
# def largest(a, b, c):
#     if a>b and a>c:
#         print(a," is a largest number")
#     elif b>a and b>c:
#         print(b," is a largest number")
#     else:
#         print(c," is a largest number")
        
# a=int(input("enter 1st number: "))
# b=int(input("enter 2nd number: "))
# c=int(input("enter 3rd number: "))
# largest(a,b,c)            


#prime number
# def prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 print(n, "is not a prime number")
#                 break
#         else:
#             print(n, "is a prime number")
#     else:
#         print(n, "is not a prime number")

# n = int(input("Enter a number: "))
# prime(n)

#sum of numbers
# def s(n):
#     s=0
#     while n>0:
#         s = s + (n % 10)
#         n=n//10
#     print("sum of number: ",s)

# n = int(input("Enter a number: "))
# s(n)        
        