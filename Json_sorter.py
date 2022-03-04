#!/usr/bin/env python
# coding: utf-8

# In[1]:


def extract_zip(path_file,root,i):
    zip_file = zipfile.ZipFile(path_file)
    for names in zip_file.namelist():
        path_files=root+"/"+ f'{i}'
        zip_file.extract(names,path_files)
        zip_file.close()
    reanaming(path_files,i)


# In[2]:


def reanaming(path_files,i):
    for root, subdirs, files in os.walk(path_files):
        for name in files:
            if name.endswith(".json"):
                os.rename(path_files+"/"+"annotations"+"/"+name, os.path.join(path_files,f'{i}' + ".json"))
                remove_files(path_files,i)


# In[3]:


def remove_files(path_files,i):
    for root, subdirs, files in os.walk(path_files):
        for name in files:
            if name.endswith(".json"):
                os.rmdir(root+"/"+"annotations")
                arr_rem(path_files,i)


# In[4]:


def arr_rem(path_files,i):
    for roots, subdirs, files in os.walk(path_files):
        for name in files:
            if name.endswith(".json"):
                if os.path.isdir(root+"/"+"Annotations"):
                    path_file = os.path.join(roots,name)
                    shutil.copy(path_file,root+"/"+"Annotations")
                else:
                    os.mkdir(root+"/" + "Annotations")
                    path_file = os.path.join(roots,name)
                    shutil.copy(path_file,root+"/"+"Annotations")
    remove_folders(path_files,i)


# In[5]:


def remove_folders(path_files,i):
    for root, subdirs, files in os.walk(path_files):
        for name in files:
            if name.endswith(".json"):
                shutil.rmtree(root+"/")


# In[6]:


def move_zip(path_files,i):
    for root, subdirs, files in os.walk(source):
        for name in files:
            if name.endswith("zip"):
                if os.path.isdir(root+"/"+"Annotations Zip"):
                    path_file = os.path.join(root,name)
                    shutil.move(path_file,root+"/"+"Annotations Zip")
                else:
                    os.mkdir(root+"/" + "Annotations Zip")
                    path_file = os.path.join(root,name)
                    shutil.move(path_file,root+"/"+"Annotations Zip")


# In[8]:


import os 
import shutil
import zipfile
import shutil
source = "C:/Users/Darvis/Downloads/HAMMAD SATTI/Annotated dataset/Ortho/Sprint 51 - Ortho - 42-LegendLinerTrials"
folder = "Sprint 51 - Ortho - 42-LegendLinerTrials"
i=1
for root , dirs, files in os.walk(source):
    for file in files:
        if file.startswith("task_sprint 51 - ortho - 42-legendlinertrials - "+ f'{i}'):
            if file.endswith('zip'):
                if os.path.isdir(root+"/"+ f'{i}'):
                    path_file = os.path.join(root,file)
                    extract_zip(path_file,root,i)
                    i=i+1
                else:
                    os.mkdir(root+"/"+ f'{i}')
                    path_file = os.path.join(root,file)
                    extract_zip(path_file,root,i)
                    i=i+1
    move_zip(source,i)


# In[ ]:




