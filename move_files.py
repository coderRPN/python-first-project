from watchdog.observers import observer
from watchdog.events import FileSystemEventHandler

import os, json, time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
        

folder_to_track = "/Users/Prabhdeep/Downloads"