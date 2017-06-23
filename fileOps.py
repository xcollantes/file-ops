# Created by Xavier Collantes
# 6/22/2017
# File: fileOps.py
# Purpose: Script to copy all leaf files child of this relative script location
# to single specified path directory.  


import os, shutil


def copy_file(pathFrom, pathTo):
    shutil.copy(pathFrom, pathTo)
    print (pathFrom + " file copied to " + pathTo)

def traverse(full_path_root):
    os.chdir(full_path_root) #Change dir to root
    
    for item in os.listdir(): #item is only name, not full path 
        if (os.path.isdir(item)):   #Case: directory
            traverse(os.path.join(full_path_root, item))
        else:                       #Case: file or leaf found 
            #FILE OPERATIONS HERE 
            copy_file(os.path.join(full_path_root, item), 'C:\\Users\\Xavier\\Desktop\\HERE')

            
            print (os.path.join(full_path_root, item) + " - processed")
       
def main():
    #ENTER DIRECTORY PATH ORIGIN/DESTINATION HERE (WHERE YOU WANT THE FILES)
    #origin is optional, default is position of script file 
    specified_origin = ''
    destination = 'C:\\Users\\Xavier\\Desktop\\HERE'

    if (specified_origin == ''):
        start_path = os.getcwd()
    else:
        start_path = specified_origin
    
    print ("Starting in " + start_path)
    traverse(start_path)
    
            
    




main()










