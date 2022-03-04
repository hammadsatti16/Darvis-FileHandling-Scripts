#import detecto
#from detecto.utils import split_video
import os
import moviepy
from moviepy.editor import *
import os
import natsort
from natsort import natsorted
import cv2
import time

L =[]

for root, dirs, files in os.walk("C:/Users/Darvis/Downloads/Trimmed videos"):

    files = natsorted(files)
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)
            #print(L)
final_clip = concatenate_videoclips(L)
final_clip.to_videofile("C:/Users/Darvis/Downloads/Combined Trimmed Video/Combined_Video.mp4", fps=24, remove_temp=False)


video = cv2.VideoCapture("C:/Users/Darvis/Downloads/Combined Trimmed Video/Combined_Video.mp4")
count = 0
index = 0
step_size=20
output_folder="C:/Users/Darvis/Downloads/frames"
folder_file_count = 500
file_count = 0
folder_count = 1
path = output_folder
os.mkdir(path+str(folder_count)+"/")
path = path+str(folder_count)+"/"

prefix= time.time()
    # Loop through video frame by frame
while True:
      ret, frame = video.read()
      if not ret:
          break
        # Save every step_size frames
      if count % step_size == 0:
          cv2.imwrite(f'{path}/{time.time()}.jpg', frame)

          index += 1
          if file_count == folder_file_count:
                    file_count = 0
                    folder_count +=1
                    path_make = output_folder + '%s' % folder_count+'/'
                    os.mkdir(path_make)
                    path = path_make
          file_count +=1

      count += 1

video.release()
cv2.destroyAllWindows()