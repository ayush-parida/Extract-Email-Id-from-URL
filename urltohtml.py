import requests
import urllib.request
import time
from bs4 import BeautifulSoup, SoupStrainer
url = input()
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
x=soup.findAll('a')
print(x)
g=open("Document.txt",'w')
g.write(str(x))
