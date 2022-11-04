#name,id,salary problem:
#name=input("enter name:")
#id=int(input("enter id:"))
#salary=float(input("enter salary:"))
#print("name is:{},id is:{},salary is:{}".format(name,id,salary))

#sum_ and _avg
#x=int(input("enter the value:"))
#y=int(input("enter the value:"))
#z=int(input("enter the value:"))
#sum=x+y+z
#avg=sum/3
#print(sum,avg,sep='\n')

#area of circle
#import math
#pi=22/7
#r=float(input("enter the value:"))
#x=pi*r**2
#print("area of circle:",x)

#get character
#x=(input("Enter a char:"))
#print("The Character is: "+x[-1])
#print("The Character is:",x[-1])

#joining of strings
#x,y=(input("enter 2 strings:")).split(",")
#print(x,y,sep="-")

#cube number
#x=float(input("enter the value:"))
#y=x**3
#print(y)

#sorting of strings
#sor=[]
#n=int(input("How many strings?"))
#for i in range(n):
#     s=input("Enter String:")
#     sor.append(s)
#sor.sort(reverse=True)
#print(sor)
#print(sor[::-1])
#print(*sor)
#for i in sor:
#     print(i)

#eval
#x=eval(input("Enter numbers:"))
#print(x,type(x))

#even_odd
#n=int(input("enter the numbers:"))
#for n in range(n):
#    if n%2 ==0:
#        print(n,"is even")
#else:
#            print(n,"is odd")

#even odd zero
#n=int(input("enter the value:"))
#if n%2 == 0:
#    print(n,'even')
#else:
#    print(n,'odd')

#print numbers from 1-10
#x=1
#while (x<=10):
#    print(x)
#    x=x+1

#even numbers from x to y range
#x=int(input())
#y=int(input())
#for i in range(x,y,2):
#     print(i)

#sum of numbers
#import math
#a,b,c,d=[float(x) for x in input("enter numbers:").split(",")]
#y=a,b,c,d
#print(sum(y)) 
 
 #multiplication of tables
#n=int(input(" Multiplication of Table: "))
#for i in range(1,11):
#    print(n,'X',i,'=',n*i)

#break loop
#n=-1
#while(n<20):
#     n+=2
#     if n>8:
#         break
#     print(n)