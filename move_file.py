import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Aashima Bandiwadekar/Downloads" # source path
to_dir = "C:/Users/Aashima Bandiwadekar/DownloadedFiles" # destination path


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event): # creating a predefined function of handler class called 'on_created' to created files  
        name,extension = os.path.splitext(event.src_path) # this line splits the path into it's name and it's extension
        for key,value in dir_tree.items(): # checking every extension value from dir_tree dictionary
            if extension in value: # if extension value equals to an extension present inside the dir_tree dictionary
                filename = os.path.basename(event.src_path) #  filename will be according to the extension mentioned above in dir_tree dictionary

                path1 = from_dir + "/" + filename # source path
                path2 = to_dir + "/" + key # destination path
                path3 = to_dir + "/" + key + "/" + filename # final path

                time.sleep(1) # set an interval of 1 second in the code

                if os.path.exists(to_dir + "/" + key ): # if destination path exists
                    if os.path.exists(path2): # if path2 or destination path exists
                        if os.path.exists(path3):
                            newfilename = os.path.splitext(filename)[0] + str(random.randint(0,9999)) + os.path.splitext(filename)[1]
                            path4 = to_dir + "/" + key+ "/" + newfilename
                            shutil.move(path1,path4)
                            time.sleep(1)
                        else:
                         shutil.move(path1,path3) # move the file from source path to destination path
                         print("moving") # print to ensure the code works
                    else: # if path2 doesn't exist
                        os.makedirs(path2) # makes folder in destination location using makedirs() function
                        shutil.move(path1,path3) #  move the file from source path to destination path
                        print("moving") # print to ensure the code works
            
# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

