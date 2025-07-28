import watchdog
import shutil
import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOADS_DIR = os.path.expanduser("~/Downloads") 
TARGET_DIR = r'C:\Users\Brayden Adcox\Posters'

class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File downloaded: {event.src_path}")
        filename = os.path.basename(event.src_path)

        if filename.endswith('.tmp'):
            print("Temporary file detected. Skipping.")
            return

        elif filename.endswith('1620.png') or filename.endswith('1620.jpg'):
            print(f"Poster detected: {filename}")
            time.sleep(1.5)
            shutil.move(event.src_path, os.path.join(TARGET_DIR, filename))
    
    def on_modified(self, event):
        filename = os.path.basename(event.src_path)

        if filename.endswith('.tmp'):
            return

        if filename.endswith('1620.png') or filename.endswith('1620.jpg'):
            print(f"[MODIFIED] Poster detected: {filename}")
            time.sleep(1.5)
            target_path = os.path.join(TARGET_DIR, filename)
            if os.path.exists(target_path):
                print(f"Already exists, skipping: {filename}")
                return
            shutil.move(event.src_path, target_path)

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(EventHandler(), path=DOWNLOADS_DIR, recursive=False)
    observer.start()
    print(f"Watching folder: {DOWNLOADS_DIR}")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopping observer...")
        observer.stop()
    observer.join()
