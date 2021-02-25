from PIL import Image
import os, sys, glob

path = '.\\resized\\delias_eucharis' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)

for item in glob.glob(".\\dataset2\\Delias eucharis\\*.jpg"):
	try:
		im = Image.open(item)
		imresize = im.resize((256, 256), Image.ANTIALIAS)
		imresize.save('{}{}{}'.format(path,'\\',os.path.split(item)[1]))
	except Exception as e:
		print(e)