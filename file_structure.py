import os
import shutil
source = "C:/Users/Darvis/Downloads/01-03-2021"
i=1
for root , dir, files in os.walk(source):
    for file in files:
        if file.endswith(".jpg"):
            if os.path.isdir(root+"/"+ "Images"):
                path_file = os.path.join(root,file)
                shutil.move(path_file,root+"/"+"Images")
            else:
                os.mkdir(root+"/"+"Images")
                path_file = os.path.join(root,file)
                shutil.move(path_file,root+"/"+"Images")
        if file.endswith(f'{i}'+".zip"):
            if os.path.isdir(root+"/"+f'{i}'+"/"+"Annotated"):
                path_file = os.path.join(root,file)
                shutil.move(path_file,root+f'{i}'+"/"+"Annotated")
                i=i+1
            else:
                os.mkdir(root+"/"+f'{i}'+"/"+"Annotated")
                path_file = os.path.join(root,file)
                shutil.move(path_file,root+"/"+f"{i}"+"/"+"Annotated")
                i=i+1
