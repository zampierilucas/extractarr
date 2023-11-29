import yaml
import logging

def read_config(config_path):
    """
    Reads a YAML configuration file and returns the settings.

    :param config_path: Path to the configuration file.
    :return: Dictionary with configuration settings.
    """
    try:
        with open(config_path, 'r') as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        print(f"Configuration file not found: {config_path}")
    except yaml.YAMLError as exc:
        print(f"Error in configuration file: {exc}")
    return {}


def setup_logging():
    """Sets up the logging configuration."""
    log_format = '%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

def log_message(level, message):
    """Logs a message with the given level."""
    if level == 'INFO':
        logging.info(message)
    elif level == 'WARN':
        logging.warning(message)
    elif level == 'ERROR':
        logging.error(message)
    else:
        logging.info(message)  # Default to INFO if level is unspecified