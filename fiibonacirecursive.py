def fibbonaci(n):
    a=0
    b=1

    if n==0 :
        return 0
    if n==1 :
        return 1
    else:
        print(fibbonaci(n-1)+fibbonaci(n-2))
    

print(fibbonaci(10))   