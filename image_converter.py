import os 
directory = r'C:/Users/Darvis/Documents/Home_deport_images/Home_deport_images' 
for filename in os.listdir(directory):
    prefix = filename.split(".png")[0]
    os.rename(filename,".jpg")