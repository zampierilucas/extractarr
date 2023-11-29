import os
import time
from watchdog.observers import Observer
from src.handler import Handler

class Watcher:
    def __init__(self, directory_to_watch, check_interval, excluded_extensions):
        self.observer = Observer()
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.CHECK_INTERVAL = check_interval
        self.EXCLUDED_EXTENSIONS = excluded_extensions

    def run(self):
        if not os.path.exists(self.DIRECTORY_TO_WATCH):
            print(f"Directory does not exist: {self.DIRECTORY_TO_WATCH}")
            return

        event_handler = Handler(self.EXCLUDED_EXTENSIONS)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(self.CHECK_INTERVAL)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()
