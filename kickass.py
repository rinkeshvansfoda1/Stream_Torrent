import requests
from bs4 import BeautifulSoup

# Note: Every Month 8th the api key changes so try to change it.
# and also if sometimes the it doesn't show the output try to make temp file free as well as try not to use the program for some time.


URL = "http://api.proxiesapi.com"

auth_key = "6563b1498ac0842e413175639ee09801_sr98766_ooPq87"

query=input("Enter the name: ")
url=f'https://kickasstorrents.to/usearch/{query}/'
# url='https://kickasstorrents.to/'

PARAMS = {'auth_key':auth_key, 'url':url} 
  
# # # sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS)

soup=BeautifulSoup(r.content,'html.parser')

# print(soup)

# name
name=[]
for i in soup.find_all(class_='cellMainLink'):
    name.append(i.text.strip())


type=[]
for i in soup.find_all('span',{'class':'font11px lightgrey block'}):
    # print(i.text.strip())
    type.append(i.text.replace("\n", " ").strip())


info=[]
for i in soup.find_all('td',{'class':'center'}):
    # print(i.text)
    info.append(i.text.strip())

a=0
k=0
j=1
# By using below two line we can fetch name  directly without insert or appending in to the list, strip function is used to remove extra spaces, replace funtion is used to replace from \n new line tag to empty by making single quote
# for i in soup.find_all(class_='cellMainLink'):
#     print(j,'-->'+i.text.strip())
for i in range(len(name)):
    print(j,"--> "+name[i])
    for i in range(0,len(info))[::5]:
        print("Size:",info[a])
        break
    for i in range(len(type)):
        print(type[k])
        break
    print("Uploaded By:",info[a+1])
    print("Age:",info[a+2])
    print("Seeder:",info[a+3])
    print("Leecher:",info[a+4])
    print()
    a=a+5
    k=k+1
    j=j+1


# for i in soup.find_all(class_='markeredBlock torType filmType'and'markeredBlock torType musicType'and'markeredBlock torType exeType'and'markeredBlock torType Type'):
# for i in soup.find_all(class_='markedBlock torType filmType'):
#     print(i.text)


href=[]
for i in soup.find_all('a',{'class':'cellMainLink'}):
    href.append('https://kickasstorrents.to'+i.get('href'))

option=int(input("Enter the choice: "))
index=href[option-1]


url=f"{index}"

URL = "http://api.proxiesapi.com"

auth_key = "6563b1498ac0842e413175639ee09801_sr98766_ooPq87"

PARAMS = {'auth_key':auth_key, 'url':url} 
  
# # sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS)

soup=BeautifulSoup(r.content,'html.parser')

magnet_link=[]
for i in soup.find_all('a',{'title':'Magnet link'}):
    magnet_link.append(i.get('href'))


title=[]
for i in soup.find_all('span',{'itemprop':'name'}):
    title.append(i.text)

import os
print(f"Playing Online.... {title[0]}")
os.system(f'peerflix "{magnet_link[0]}" --vlc')