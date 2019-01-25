import os
import shutil       # The only modules we'll import

path = r"C:/Users/lksfi/Downloads/"      # I am sorting files from my downloads folder, however, this directory can be changed to anything you want.
names = os.listdir(path)
folder_name = ['image', 'pdf', 'word docs']           # I am sorting images and .pdf files into their own folders. 
for x in range(0, 2):
        if not os.path.exists(path+folder_name[x]):   # This for loop makes it so no folders or files are overwritten. 
                os.makedirs(path+folder_name[x])
for files in names:                                                           # This moves the png, pdf, jpg, and docx files into their respective folders if they aren't already there.
        if '.png' in files and not os.path.exists(path+'image/'+files):
                shutil.move(path+files, path+'image/'+files)
        if '.pdf' in files and not os.path.exists(path+'pdf/'+files):
                shutil.move(path+files, path+'pdf/'+files)
        if '.jpg' in files and not os.path.exists(path+'image/'+files):
                shutil.move(path+files, path+'image/'+files)
        if '.docx' in files and not os.path.exists(path+'word docs/'+files):
                shutil.move(path+files, path+'word docs/'+files)