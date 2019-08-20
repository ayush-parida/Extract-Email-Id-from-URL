from bs4 import BeautifulSoup, SoupStrainer
a=[]
with open('Document.txt','r') as f:
    for link in BeautifulSoup(f.read(), parse_only=SoupStrainer('a')): 
        if link.has_attr('href'): 
            print(link['href'])
            a.append(link['href'])
f=open("new.txt","w")
count1=0
for i in range (len(a)):
    b=a[i]
    if'www'in b:
        head,sep,tail=b.partition('=')
        x,y,z=tail.partition('.com')
        f.write(x+".com\n")
        count1+=1
f.close()
print(count1)
