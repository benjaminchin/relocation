import shutil
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        direc = os.listdir(folder_to_track)
        for filename in direc:
            if filename[:-3] == 'osz':
                src = folder_to_track + '/' + filename
                dst = folder_dst + '/' + filename
                os.rename(src, dst)
                print('File Moved')

folder_to_track = 'E:/Downloads'
folder_dst = 'E:/Games/osu!/Songs'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=False)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
print('What')
