import cv2
import time
import os
import moviepy
from moviepy.editor import *
import natsort
from natsort import natsorted
import cv2
import time
from tqdm import tqdm
count = 0
index = 0
step_size=20
output_folder="C:/Users/Darvis/Downloads/frames"
folder_file_count = 500
file_count = 0
src="/C:/Users/Darvis/Downloads/Trimmed videos"
folder_count = 1
path = output_folder
os.mkdir(path+str(folder_count)+"/")
path = path+str(folder_count)+"/"
total_videos =len(os.listdir("C:/Users/Darvis/Downloads/Trimmed videos"))
current_video = 0
total_frames = 0
for vid in tqdm(os.listdir("C:/Users/Darvis/Downloads/Trimmed videos")):
      current_video+=1
      if not vid.endswith("mp4"):continue
      video = cv2.VideoCapture(f'{"C:/Users/Darvis/Downloads/Trimmed videos"}/{vid}')
      prefix= time.time()
      while True:
              ret, frame = video.read()
              if not ret:
                  break
        # Save every step_size frames
              if count % step_size == 0:
                  images=cv2.imwrite(f'{path}/{time.time()}.jpg', frame)

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