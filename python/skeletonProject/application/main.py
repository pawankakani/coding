import logging
from core.utils import some_reusable_function

app_logger = logging.getLogger('application_logger')

def start_application(config):
    """
    Main function to start the application.
    It reads the config and uses a reusable module.
    """
    app_logger.info("Application started.")
    app_logger.info(f"Using a setting from config: {config['project_name']}")
    
    # Example of using a reusable module
    some_reusable_function()
    
    app_logger.info("Application finished.")