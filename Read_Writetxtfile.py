def read():
    f1=open("textfile.txt","r")
    s=f1.read()
    print(s)
    f1.close()

def write():
    f1=open("textfile.txt","w")
    s=input("enter what you want to insert in the file")
    f1.write(s)
    f1.close()


def readline():
     f1=open("textfile.txt","r")
     s=f1.readlines()
     print(s)
     #this returns the text in a list(array)

def writelines():
     l=[]
     f2=open("textfile.txt","w+") 
     a=int(input("how many lines you want to add in the file"))
     for i in range(a):
          line=input("Enter Your line")
          l.append(line+"\n")
        