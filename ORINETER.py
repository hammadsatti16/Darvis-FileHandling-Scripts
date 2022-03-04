from tqdm import tqdm_notebook as tqdm 
import os
from PIL import Image
from PIL.ExifTags import TAGS

# replace below with image directory
image_dir = 'C:/Users/Darvis/Downloads/frames1/'

for image in os.listdir(image_dir):

  image_path = image_dir + image
  im = Image.open(image_path)
  im = im.rotate(90)
  im = im.rotate(180)
  im.save(image_path)