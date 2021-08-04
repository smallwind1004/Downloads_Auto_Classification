from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import shutil
import time
# import json
skip = ['crdownload', 'tmp', 'TMP']

class Myhandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            file_type = filename.split('.')[-1].lower()
            print(file_type)
            time.sleep(1)
            if file_type not in skip:
                if file_type not in os.listdir(folder_destimation):
                    os.mkdir(folder_destimation + "/" + file_type + "")
                src = folder_to_track + "/" + filename
                new_destinmation = folder_destimation + "/" + file_type + "/" + filename
                shutil.move(src, new_destinmation)


folder_to_track = 'C:/Users/smallwind/Downloads'
folder_destimation = 'D:/Downloads'
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join