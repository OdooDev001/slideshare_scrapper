import requests
from bs4 import BeautifulSoup
import urllib


URL = input("enter slideshare file url")
filename = input("enter file name")
try:
    r = requests.get(URL)
except:
    print("error while feching url")
    
soup = BeautifulSoup(r.content, 'html5lib')

quotes=[]
count = 0 
table = soup.find('div', attrs = {'id':'stage'})
for row in table.findAll('img'):
    count +=1
    urllib.request.urlretrieve(row["src"],f"{filename}{count}.jpg")
    print(f"##### {filename}{count} ### downloaded")
    
print("##### completed #####")
