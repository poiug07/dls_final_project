import argparse
import glob
from PIL import Image
import random

parser = argparse.ArgumentParser(description='Download images from bing search.')
parser.add_argument('path', required=True, action='store', type=str, help='The path to folder with images.')

args = parser.parse_args()

path = args.path

for i, item in enumerate(glob.glob(path+'\\*.jpg')):
	image = Image.open(item)
	degree = random.randint(-20, 20)
	image = image.rotate(degree)
	image.save(item[:-4]+'_r.jpg')
	print('finished', i+1, 'image')