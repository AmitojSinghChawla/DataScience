def binarysearch(l,no):
    flag=0
    start=0
    last=len(l)-1
    while start<=last:
        mid=(start+last)//2
        if l[mid]==no:
            flag=1
            return
        elif l[mid]<no:
            start=mid+1
        else:
            start=mid-1

    if flag==1:
        print(f"found the no in the list")

    else:  
        print(f"not found")          

#This is a Binary Search Program
print(f'please enter a list')
L=[10,5,9,11,14,17,19,32,18,74,62,39]
L.sort()
print("Enter the No yo Want to Search in the list")
number=eval(input("--->"))
print(binarysearch(L,number))