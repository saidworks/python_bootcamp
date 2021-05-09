# get json object => found it window_sharedData
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
url = "https://instagram.frba4-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/183211053_953862335418778_8177150041903874595_n.jpg?tp=1\u0026_nc_ht=instagram.frba4-1.fna.fbcdn.net\u0026_nc_cat=110\u0026_nc_ohc=gf3VJOgi178AX-L1vdM\u0026edm=AABBvjUBAAAA\u0026ccb=7-4\u0026oh=3e5f22dad8d517d4c05039b51516dcd3\u0026oe=60BC8836\u0026_nc_sid=83d603"
url = url.replace("\\u0026","&")
insta = requests.get(url)

 #create the image
# test_img = open('image.jpg','wb')
insta_img = open('insta.jpg','wb')
# test_img.write(test.content)
insta_img.write(insta.content)










