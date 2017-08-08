# Created by Xavier Collantes
# 6/22/2017
# File: fileOps.py


import os, shutil, sys

def copy_file(pathFrom, pathTo):
    shutil.copy(pathFrom, pathTo)
    print (pathFrom + " file copied to " + pathTo)

# Purpose: Script to copy all leaf files child of this relative script location
# to single specified path directory.  
def traverse(full_path_root):
    os.chdir(full_path_root) #Change dir to root
    
    for item in os.listdir(): #item is only name, not full path 
        if (os.path.isdir(item)):   #Case: directory
            traverse(os.path.join(full_path_root, item))
        else:                       #Case: file or leaf found 
            #FILE OPERATIONS HERE 
            copy_file(os.path.join(full_path_root, item), 'C:\\Users\\Xavier\\Desktop\\HERE')

            
            print (os.path.join(full_path_root, item) + " - processed")

# pre: Directory with contents
# post: output file populated with directory file names
# purpose: output all filenames to a specified file 
def getPaths(full_path, destination):
    os.chdir(full_path)
    
    #File Operations 
    fo = open(destination, 'w+')

    for i in os.listdir(full_path):
        raw = str(i)
        fo.write(raw + ", " + "\n")

    fo.close()
    
def main():
    #ENTER DIRECTORY PATH ORIGIN/DESTINATION HERE (WHERE YOU WANT THE FILES)
    #origin is optional, default is position of script file
    specified_origin = ''
    destination = ''


    print ("Origin: " + specified_origin)
    print ("Destination: " + destination)
    start = input("Confirm origin/destination paths (y/n)?")
    if (start == 'Y' or start == 'y'):
        if (specified_origin == ''):
            start_path = os.getcwd()
        else:
            start_path = specified_origin
    
        print ("Starting in " + start_path)
        #traverse(start_path)
        getPaths(specified_origin, destination)


        
    else:
        print ("Please check paths are correct in src file.")
        
   
    
            
    




main()










