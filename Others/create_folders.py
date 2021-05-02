import os

#path
path = './'

#create lists
folders = ['day'+str(i) for i in range(18,20,1)]

#make directories
for folder in folders:
    os.makedirs(os.path.join(path,folder))
