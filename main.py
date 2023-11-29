import os
from src.watcher import Watcher
from src.utils import read_config
from src.utils import setup_logging

def main():
    # Configure logging
    setup_logging()

    # Load configuration
    config = read_config(os.path.expanduser('~/.config/extractarr/config.yml'))

    # Extract relevant settings
    watch_directories = config.get('watch_directories', [])
    check_interval = config.get('check_interval', 5)

    # Check if any directories are configured for watching
    if not watch_directories:
        print("No directories are configured for watching. Please update the config.yml file.")
        return

    # Initialize and start the watcher for each directory
    for directory in watch_directories:
        print(f"Starting to watch: {directory}")
        watcher = Watcher(directory, check_interval)
        watcher.run()

if __name__ == '__main__':
    main()