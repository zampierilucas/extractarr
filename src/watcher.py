import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from patoolib import extract_archive
from src.utils import log_message
import threading

class Watcher:
    def __init__(self, directory_to_watch, check_interval):
        self.observer = Observer()
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.CHECK_INTERVAL = check_interval

    def run(self):
        if not os.path.exists(self.DIRECTORY_TO_WATCH):
            print(f"Directory does not exist: {self.DIRECTORY_TO_WATCH}")
            return

        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(self.CHECK_INTERVAL)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            file_name = os.path.basename(event.src_path)
            log_message('INFO', f"New file detected: {file_name}")
            Handler.handle_file(event.src_path)

    @staticmethod
    def handle_file(file_path):
        file_name = os.path.basename(file_path)
        log_message('INFO', f"Processing file: {file_name}")

        # Start a new thread to check if the file is complete
        file_check_thread = threading.Thread(target=Handler.wait_until_download_completes, args=(file_path,))
        file_check_thread.start()

    @staticmethod
    def extract_file(file_path):
        try:
            extract_path = os.path.splitext(file_path)[0]
            os.makedirs(extract_path, exist_ok=True)
            extract_archive(file_path, outdir=extract_path, verbosity=-1,interactive=False)
            log_message('INFO', f"Extracted: {os.path.basename(file_path)}")
        except Exception as e:
            log_message('ERROR', f"Error processing {os.path.basename(file_path)}: {e}")

    @staticmethod
    def wait_until_download_completes(file_path, check_interval=1, stable_period=5):
        last_size = -1
        stable_for = 0

        while stable_for < stable_period:
            try:
                current_size = os.path.getsize(file_path)
                if current_size == last_size:
                    stable_for += check_interval
                else:
                    stable_for = 0
                    last_size = current_size

                time.sleep(check_interval)
            except FileNotFoundError:
                log_message('ERROR', f"File not found during checking: {file_path}")
                return

        # File is stable, proceed with extracting
        Handler.extract_file(file_path)