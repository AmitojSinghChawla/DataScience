print("Program to calculate your average in maths physic and english ")
print("press 1 to Continue")
decision=int(input(":->"))
if decision == 1 :
    print("enter Your Marks for English Maths and Physics Respectively;") 
    a=float(input())
    b=float(input())
    c=float(input())
     
    sum= a+b+c
    average=int(sum/3)
    print("your Average is ",average)

else:
    print("wrong Input")

    