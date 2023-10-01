import os
import pathlib
import shutil
  
# This is to get the directory that the program  
# is currently running in. 

dir_path = os.path.realpath('E:\TORRENTZ\Pmv Ark')
file_list = open('E:\\TORRENTZ\Pmv Ark\\redownload.txt', "a")
EMPTY_FILE = os.path.realpath('E:\TORRENTZ\Pmv Ark\[Empty Files]')

for root, dirs, files in os.walk(dir_path): 
    for file in files:
  
        # change the extension from '.mp3' to  
        # the one of your choice. 
        
        if os.path.getsize(root+'\\'+file) == 0: 
            file_list.write(pathlib.PurePath(root).name + ' ' + file + '\n')
            if os.path.exists(EMPTY_FILE) is not True:
                os.mkdir(EMPTY_FILE)
            shutil.move(root+'\\'+str(file), EMPTY_FILE)
            print (root+'\\'+str(file))

file_list.close()