import csv

f1=open("record.csv","r+")
cs=csv.reader(f1,delimiter=",")
for row in cs :
    print(row)

f1.close()    