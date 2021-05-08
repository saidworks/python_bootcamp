#study how instagram store their images
# get url of an image
# get package to download the content of image
#store image
#save it as a file

import requests
import urllib
test = requests.get('https://upload.wikimedia.org/wikipedia/commons/5/58/Fun._band.jpg')
insta = requests.get('https://instagram.fcmn5-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/182344864_503717724396957_3533310441711211111_n.jpg?tp=1&_nc_ht=instagram.fcmn5-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=xuAXBU7N1qEAX9zHpeY&edm=AABBvjUBAAAA&ccb=7-4&oh=8df2e43ebf9b6e351fd40c9ee45a8972&oe=60BCC80D&_nc_sid=83d603')
test_img = open('image.jpg','wb')
insta_img = open('insta.jpg','wb')
test_img.write(test.content)
insta_img.write(insta.content)

web = urllib.request.urlopen("https://www.instagram.com/p/COkrpEBFYfnvtXj1deEjJheB7I9i0ZGBEXX_xQ0/")


print(web)