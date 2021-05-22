# get json object => found it window._sharedData
# in the post page look for "PostPage" then "src" property
# reformat url replace "\u0026" wtih "&"
# use requests to get the data as binary
# store requests response in a file that was created before as jpg using b params
#store image
# #save it as a file
#
import requests
#scrap the url of the picture



#get image with requests
# test = requests.get('https://upload.wikimedia.org/wikipedia/commons/5/58/Fun._band.jpg')
#use requests.get to get a response as binary content that can be transformed to image
url = "https://instagram.frba3-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s750x750/189096643_650802222450710_104471476791829754_n.jpg?tp=1\u0026_nc_ht=instagram.frba3-2.fna.fbcdn.net\u0026_nc_cat=1\u0026_nc_ohc=8NM0B3vA0n0AX97iTXj\u0026edm=AABBvjUBAAAA\u0026ccb=7-4\u0026oh=9d4807556d73ea52bdb6837460b053c4\u0026oe=60AFE4B1\u0026_nc_sid=83d603"
url = url.replace("\\u0026","&")
insta = requests.get(url)

 #create the image
# test_img = open('image.jpg','wb')
insta_img = open('insta.jpg','wb')
# test_img.write(test.content)
insta_img.write(insta.content)










