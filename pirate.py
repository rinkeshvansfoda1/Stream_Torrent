import requests
from requests.models import ContentDecodingError 
from bs4 import BeautifulSoup

# Note: Every Month 8th the api key changes so try to change it.

URL = "http://api.proxiesapi.com"

auth_key = "6563b1498ac0842e413175639ee09801_sr98766_ooPq87"

query=input("Enter the movie name: ")
url = f"https://thepiratebay0.org/search/{query}/1/99/0"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'auth_key':auth_key, 'url':url} 
  
# # # sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS)
  
soup=BeautifulSoup(r.content,'html.parser')

# seeder and leecher
seed_peers=[]
for i in soup.find_all('td',{'align':'right'}):
    seed_peers.append(i.text)

seeder=[]
leecher=[]

for i in seed_peers[0::2]:
    seeder.append(i)

for i in seed_peers[1::2]:
    leecher.append(i)

# info
info=[]
for i in soup.find_all({'font':'detDesc'}):
    info.append(i.text)

# # to delete element by indexing
# # del(info[1::2])


# # lsst=['Uploaded 12-18\xa02021, Size 2.53\xa0GiB, ULed by  xxxlavalxxx ', 'xxxlavalxxx', 'Uploaded 01-21\xa004:33, Size 3.02\xa0GiB, ULed by  sotnikam ', 'sotnikam', 'Uploaded 12-16\xa02021, Size 1.27\xa0GiB, ULed by  shmasti ', 'shmasti', 'Uploaded 01-10\xa014:51, Size 2.12\xa0GiB, ULed by Anonymous', 'Uploaded 12-27\xa02021, Size 2.61\xa0GiB, ULed by  B4ND1T69 ', 'B4ND1T69', 'Uploaded 12-25\xa02021, Size 1.87\xa0GiB, ULed by  B4ND1T69 ']
# # b='Anonymous'
# # for i in lsst:
# #     w=i.find(b)
# #     print(w)


# # name and other info
name=[]
j=1
a=0
for i in soup.find_all(class_='detName'):
    name.append(i.text)
    print(j,'-->'+i.text)
    for i in range(len(seeder)):
        print("Seeder:",seeder[a])
        break
    for i in range(len(leecher)):
        print("Leecher:",leecher[a])
        break
    for i in range(len(info)):
        print(info[a])
        break
    print()
    a=a+1
    j=j+1


# link
href=[]
for i in soup.find_all(class_='detLink'):
    href.append(i.get('href'))

option=int(input("Enter the choice: "))
index=href[option-1]

url=f'{index}'

URL = "http://api.proxiesapi.com"

auth_key = "6563b1498ac0842e413175639ee09801_sr98766_ooPq87"

# # # # defining a params dict for the parameters to be sent to the API 
PARAMS = {'auth_key':auth_key, 'url':url} 
  
r = requests.get(url = URL, params = PARAMS)
soup=BeautifulSoup(r.content,'html.parser')

magnet_link=[]
for i in soup.find_all('a',{'title':'Get this torrent'})[0:1]:
    magnet_link.append(i.get('href'))

title=[]
for i in soup.find_all('div',{'id':'title'}):
    title.append(i.text)

import os
print(f"Playing Online....{title[0]}")
os.system(f'peerflix "{magnet_link[0]}" --vlc')





# each and every field
# top_100='https://thepiratebay0.org/top/all'
# audio_top100='https://thepiratebay0.org/top/100'
# video_top100='https://thepiratebay0.org/top/200'
# application_top100='https://thepiratebay0.org/top/300'
# games_top100='https://thepiratebay0.org/top/400'
# Adult_top100='https://thepiratebay0.org/top/500'
# other_top100='https://thepiratebay0.org/top/600'


# def method(url):
#     URL = "http://api.proxiesapi.com"

#     auth_key = "72cd451dabffa866f635377ab677a708_sr98766_ooPq87"
#     PARAMS = {'auth_key':auth_key, 'url':url} 
  
# # # sending get request and saving the response as response object 
#     r = requests.get(url = URL, params = PARAMS)
  
#     soup=BeautifulSoup(r.content,'html.parser')

#     seed_peers=[]
#     for i in soup.find_all('td',{'align':'right'}):
#         seed_peers.append(i.text)

#     a=0
#     seeder=[]
#     leecher=[]

#     for i in seed_peers[0::2]:
#         seeder.append(i)

#     for i in seed_peers[1::2]:
#         leecher.append(i)

#     info=[]
#     for i in soup.find_all({'font':'detDesc'}):
#         info.append(i.text)

#     # to delete element by indexing
#     # del(info[1::2])


# # lsst=['Uploaded 12-18\xa02021, Size 2.53\xa0GiB, ULed by  xxxlavalxxx ', 'xxxlavalxxx', 'Uploaded 01-21\xa004:33, Size 3.02\xa0GiB, ULed by  sotnikam ', 'sotnikam', 'Uploaded 12-16\xa02021, Size 1.27\xa0GiB, ULed by  shmasti ', 'shmasti', 'Uploaded 01-10\xa014:51, Size 2.12\xa0GiB, ULed by Anonymous', 'Uploaded 12-27\xa02021, Size 2.61\xa0GiB, ULed by  B4ND1T69 ', 'B4ND1T69', 'Uploaded 12-25\xa02021, Size 1.87\xa0GiB, ULed by  B4ND1T69 ']
# # b='Anonymous'
# # for i in lsst:
# #     w=i.find(b)
# #     print(w)


# # name and other info
#     name=[]
#     j=1
#     a=0
#     for i in soup.find_all(class_='detName'):
#         name.append(i.text)
#         print(j,'-->'+i.text)
#         for i in range(len(seeder)):
#             print("Seeder:",seeder[a])
#             break
#         for i in range(len(leecher)):
#             print("Leecher:",leecher[a])
#             break
#         for i in range(len(info)):
#             print(info[a])
#             break
#         print()
#         a=a+1
#         j=j+1

#     # link
#     href=[]
#     for i in soup.find_all(class_='detLink'):
#         href.append(i.get('href'))

#     option=int(input("Enter the choice: "))
#     index=href[option-1]

#     url=f'{index}'

#     URL = "http://api.proxiesapi.com"

#     auth_key = "72cd451dabffa866f635377ab677a708_sr98766_ooPq87"

#     # # # # defining a params dict for the parameters to be sent to the API 
#     PARAMS = {'auth_key':auth_key, 'url':url} 
    
#     r = requests.get(url = URL, params = PARAMS)
#     soup=BeautifulSoup(r.content,'html.parser')

#     magnet_link=[]
#     for i in soup.find_all('a',{'rel':'nofollow'})[0:1]:
#         magnet_link.append(i.get('href'))
#         # print(i.get('href'))


#     import os
#     print("Playing Online....")
#     os.system(f'peerflix "{magnet_link[0]}" --vlc')


# print("1. Top 100")
# print("\n2. Audio Top 100")
# print("\n3. Video Top 100")
# print("\n4. Application Top 100")
# print("\n5. Games Top 100")
# print("\n6. Adult Top 100")
# print("\n7. Other/E-book Top 100")
# print("\n8. Search")

# i=int(input("Enter the Choice: "))
# if i==1:
#     method(top_100)
# elif i==2:
#     method(audio_top100)
# elif i==3:
#     method(video_top100)
# elif i==4:
#     method(application_top100)
# elif i==5:
#     method(games_top100)
# elif i==6:
#     method(Adult_top100)
# elif i==7:
#     method(other_top100)
# elif i==8:
#     query=input("Enter the name: ")
#     url=f"https://thepiratebay0.org/search/{query}/1/99/0"
#     method(url)
# else:
#     print("Please Select correct Option")