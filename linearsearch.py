print("This is a linear Search Program")

a=[10,20,30,5,8,9,7,6,5,4,3,2,19,23,27]
list=a.sort()
print(f"sorted list is {list}")


#first we sort the list
d=len(a)


#input no to find out
print(f"Enter the no to check for in the list")
number=int(input("--->"))

for i in range(d):
    if a[i]==number:
             print(f"No Found at Index{i}")

    else:
             print(f"No SUch No exsits in the list")
             break    

