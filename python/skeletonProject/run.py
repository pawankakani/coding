import yaml
import logging.config
import logging
from application.main import start_application

def setup_logging(config_path='config.yaml'):
    """Sets up logging from the configuration file."""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config['logging'])
    except FileNotFoundError:
        logging.basicConfig(level=logging.INFO)
        logging.warning("Config file not found. Using default logging configuration.")

def read_config(config_path='config.yaml'):
    """Reads project configuration from a YAML file."""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            return config['app_settings']
    except FileNotFoundError:
        logging.error("Configuration file not found. Exiting.")
        return None

if __name__ == "__main__":
    setup_logging()
    app_config = read_config()
    if app_config:
        start_application(app_config)