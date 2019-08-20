import urllib.request,re
import csv
c=open('new.txt','r')
a=[]
x=[]
for i in range(7):
    f = urllib.request.urlopen(c.readline())
    s = f.read().decode('utf-8')
    print(re.findall(r"\+\d{2}\s?0?\d{10}",s))
    print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s))
    m=(re.findall(r"\+\d{2}\s?0?\d{10}",s))
    n=(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s))
    x.append(n)
myFile = open('example2.csv', 'w', newline='')
with myFile:
    for i in x:
        for j in i:
            c=[[j]]
            print(c,i)
            writer = csv.writer(myFile)
            writer.writerows(c)
