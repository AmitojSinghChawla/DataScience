import csv

feilds=["rollno","standard","phone"]
N=int(input("enter how many records you want to add-->"))
rows=[]
for i in range(N):
    Rno=int(input("enter your ROll No-->"))
    name=input("Enter Your Name-->")
    standard=input("enter your standard-->")
    record=[Rno,name,standard]
    rows.append(record)

f1=open("record.csv","w+")
cs=csv.writer(f1)
cs.writerow(feilds)


for i in rows:
    cs.writerow(i)

f1.close()  