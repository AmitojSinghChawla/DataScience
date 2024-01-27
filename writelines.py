def writelines():
    l=[]
    f2=open("textfile.txt","w")
    print("how many lines you want to add in the file")
    a=int(input("-->"))
    for i in range(a):
        print("enter your lines")
        line=input("--->")
        l.append(line+"\n")
        

    f2.writelines(l)
    f2.close()

writelines()

        
        
        
