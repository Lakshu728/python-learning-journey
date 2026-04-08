#Create a tuple with 5 numbers and print it
# t=()
# for i in range(5):
#      num = int(input(f"Enter number {i+1}: "))
#      t = t + (num,)
# print("\nTuple is:", t)

# print(t *3) #print tuple three times

#length of tuple without using len() function
# t=(1,2,3,4,5,6)
# c=0
# for i in t:
#     c=c+1
# print("Length of tuple is:", c)  

#Convert tuple into list and modify one element
# a=(1,2,3,4,5,6)
# print(list(a))
# b=list(a)
# b.append(34)
# print("list is",b)
# d= tuple(b)
# print ("before convert tuple is",d)


#Find the index of element 10 in a tuple
# a=(1,2,3,6,8,10)
# print(a.index(10))

#Create a single-element tuple
# t=(1,)
# print("single element",t)

#Concatenate two tuples and print resul
# a=(1,2,3)
# b=(4,5,6)
# print("concatenate two tuples: ",a+b)

#Unpack tuple into 3 variables
# a, b, c=(1,2,3)
# print(a,b,c)

#Find maximum and minimum value in tuple
# t=()
# for i in range(5):
#      num = int(input(f"Enter number {i+1}: "))
#      t = t + (num,)
# print("\nTuple is:", t)
# max=t[0]
# min=t[0]

# for num in t:
#     if num > max:
#        max=num
#     if num < min:
#        min=num
# print("Maximum number:", max)
# print("Minimum number:", min)


#reverse tuple
# a=(1,2,3)
# b=list(a)
# b.reverse()
# d =tuple(b)
# print("reverse tuple is : ",d)

#sort tuple
# a=(13,56,78,98,76,3,4)
# b=list(a)
# b.sort()
# d =tuple(b)
# print("sort tuple is : ",d)

#Count even and odd numbers in tuple
# a=(13,56,78,98,76,3,4)
# even=0
# odd=0
# for i in a:
#     if i%2==0:
#         even=even+1
#     else :
#         odd=odd+1
# print("Even numbers:", even)
# print("Odd numbers:", odd)        
        
        
#merge tuple without using +        
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# t3 = ()
# for i in t1:
#     t3 = t3 + (i,)
# for i in t2:
#     t3 = t3 + (i,)
# print("Merged tuple:", t3)        