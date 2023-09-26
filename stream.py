import requests
from requests.models import ContentDecodingError 
from bs4 import BeautifulSoup


URL = "http://api.proxiesapi.com"

# Note: The API key sometimes changes so, when we get nothing in output while printing then consider to change API key from 'https://app.proxiesapi.com/index.php' 
# insert your auth key here
auth_key = "72cd451dabffa866f635377ab677a708_sr98766_ooPq87"
# 65e50c4003ded60462725f908db49b59_sr98766_ooPq87
query=input("Enter the movie name: ")
url = f"https://www.1337x.to/search/{query}/1/"

# url = "https://www.1337x.to/search/bharat/1/"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'auth_key':auth_key, 'url':url} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS)
  
# print(r.text)
soup=BeautifulSoup(r.content,'html.parser')

main=[]
# last=soup.find('li',{'class':'last'})
# print(last.text)
for i in soup.find_all('td'):
    # print(i.text)
    main.append(i.text)
# print(main[0:5:])

# for i in main[:20]:
# print(index)
print(['Name', 'Seeder', 'Leacher', 'Date', 'Size'])
j=0
index=1
# here [:20] are used to get the starting 20 values
# for i in range(len(main))[:20]:
#     i=j
#     print(index,main[i:i+5:])
#     j+=6
#     index+=1


# for getting exact first page without giving other empty list from the first page upper alternative
for i in range(len(main)):
    i=j
    if main[i:i+5]:
        print(index,main[i:i+5])
        # break
    else:
        # print(index,main[i:i+5])
        break
    j+=6
    index+=1


# j=1
# for i in range(20):
#     i=j
#     print(i)
#     j+=2

# name=main[0::6]
# seeder=main[1::6]
# leacher=main[2::6]
# size=main[4::6]
# p=0
# q=0
# r=0
# s=0
# for i in range(len(name)):
#     print("Name: ",name[i])
#     for j in range(len(seeder)):
#         print("Seeder: ",seeder[j])
#         for k in range(len(leacher)):
#             print("Leacher: ",leacher[k])
#             for n in range(len(size)):
#                 print("Size: ",size[n])


href=[]
for link in soup.find_all('a')[33:-16:3]:
    # print("https://www.1337x.to"+link.get('href'))
    href.append("https://www.1337x.to"+link.get('href'))
# print(href)

option=int(input("Enter the number you want: "))
index=href[option-1]
# for checking purpose we are printing two times the url from below and then after by giving upper index value to below url variable
# print(index)


url=f'{index}'
print(url)


# url = "https://www.1337x.to/torrent/3807197/Bharat-2019-Hindi-720p-pDVDRip-x264-AAC-Ads-Blurred/"
# print(url)

URL = "http://api.proxiesapi.com"

auth_key = "72cd451dabffa866f635377ab677a708_sr98766_ooPq87"

# # defining a params dict for the parameters to be sent to the API 
PARAMS = {'auth_key':auth_key, 'url':url} 
  
# # sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS)
soup=BeautifulSoup(r.content,'html.parser')
# print(r.content)

# Note: Address of different class object under div are changing and below both are working fine only we need to change class name starting from 'c' variable then onwards
# a=soup.find('div',{'class':'row'})
# b=a.find('div',{'class':'col-9 page-content'})
# c=b.find('div',{'class':'box-info torrent-detail-page vpn-info-wrap'})
# d=c.find('div',{'class':'l968a4eb4bfc52673c5c50ff9fa238dc3be55ce9d no-top-radius'})
# e=d.find('div',{'class':'l87dafbf081a8d027f5b05685474dfabdeb942cff clearfix'})
# f=e.find('ul',{'class':'l507889aaa3041b21b8f53f0ca47b9cf4bfd642e6 l6c8633a39f6e5c92f28ec437e8b2d09d0b07877e'})
# for i in f.find_all('a',{'class':'l38cc013201ff55e74c582988ddbbdd423fffec4a l667827fcf4a0bd6d4a4f843a8d33fcf9473292b1 l7a5ff21b11cb85e4d1de83f2ceaf3451e1741bf1'}):
#     print(i.get('href'))


# lsts=[]
# for i in a.find_all('a',{'class':'l320ada3f2776accf5a1ebb37cc5437be8c9c25d3 la9a434c07e187c3aba3da860a639e4c8e64529c3 lb2694025b2b16ee8d688acd3fd8cb9471e6251ba'}):
#     # print(i.get('href'))
#     lsts.append(i.get('href'))
# print(lsts[0])


a=soup.find('div',{'class':'row'})
lsts=[]
for i in a.find_all('a'):
    # print(i.get('href'))
    lsts.append(i.get('href'))
# print(lsts[22])
a=lsts[22]

import os
# print(f'peerflix "{a}" --vlc')
# a=(f'peerflix "{a}" --vlc')
# print(a)
os.system(f'peerflix "{a}" --vlc')