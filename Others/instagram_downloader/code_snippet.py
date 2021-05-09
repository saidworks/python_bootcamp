# # get json object => found it window_sharedData
# # in the post page look for "PostPage" then "src" property
# # reformat url replace "\u0026" wtih "&"
# # use requests to get the data as binary
# # store requests response in a file that was created before as jpg using b params
# #store image
# # #save it as a file
# #
# import requests
# import urllib
# from bs4 import BeautifulSoup
# # test = requests.get('https://upload.wikimedia.org/wikipedia/commons/5/58/Fun._band.jpg')
# url = "https://instagram.frba4-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/183211053_953862335418778_8177150041903874595_n.jpg?tp=1\u0026_nc_ht=instagram.frba4-1.fna.fbcdn.net\u0026_nc_cat=110\u0026_nc_ohc=gf3VJOgi178AX-L1vdM\u0026edm=AABBvjUBAAAA\u0026ccb=7-4\u0026oh=3e5f22dad8d517d4c05039b51516dcd3\u0026oe=60BC8836\u0026_nc_sid=83d603"
# url = url.replace("\\u0026","&")
# insta = requests.get(url)
#
# # test_img = open('image.jpg','wb')
# # insta_img = open('insta.jpg','wb')
# # test_img.write(test.content)
# # insta_img.write(insta.content)
#
#
# # soup = BeautifulSoup(insta.content,features="lxml")
# # finder = soup.find('sharedData')
# # print(url)
# #
# # print(soup)
# import json
# try:
#     from urllib.parse import urlparse
# except ImportError:
#     from urlparse import urlparse
#
# BASE_URL = 'https://www.instagram.com/szitouni/'
# CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
#
# session = requests.Session()
# session.headers = {'user-agent': CHROME_WIN_UA, 'Referer': BASE_URL}
# session.cookies.set('ig_pr', '1')
# req = session.get(BASE_URL)
# session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
#
#
# url = "https://www.instagram.com/p/COqnAAolmCv/"
# response = session.get(url, cookies="", headers={'Host': urlparse(url).hostname}, stream=False, timeout=90)
# json_response = response.json()
#
# print(json_response)


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Navigate to Url
driver.get("https://www.instagram.com/")

# Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

for e in elements:
    print(e.text)
