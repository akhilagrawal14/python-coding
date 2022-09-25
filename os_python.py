import os 
import glob

path=r"D:\project\python coding"
directory=r"D:\project\python coding\python"    
file_path="abc.txt" 


def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")
        
def remove_dir(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
    except OSError:
        print(f"ERROR: deleting directory with name {path}")

#get files in all  directories and subdirectories with extension in '.txt' like that
def get_files(path,extension):
    path=extension+"/**/*"+extension
    #path = r'E:/account/**/*.txt' #example
    files = glob.glob(path, recursive=True)


# Get the current working 

cwd = os.getcwd() 

# Changing the Current working directory to '../'
os.chdir('../') 


# make directory , better if some ittermidiate directory missing it makes it
os.makedirs(path)

## if not exist make directory
if not os.path.exists(directory):
    os.makedirs(directory)

#list all files in path, in black it is current path
os.listdir(path) 

#remove a file
os.remove(file_path)

##better way
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("The system cannot find the file specified")

#remove a directory, can't if not empty
os.rmdir(directory)

#remove directory with all files


import shutil
shutil.rmtree() 
# it is used to delete an entire directory tree,
# path must point to a directory (but not a symbolic link to a directory) ex. mid directory



# can even remove all txt/jpg file in path

filelist = glob.glob(os.path.join(directory, "*"))
for f in filelist:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))
# then use rmdir if exist for folder

#size 
os.path.getsize("filename")

## get basename of file folder
os.path.basename(path)

#for directory path of that path ex file
os.path.dirname(path)