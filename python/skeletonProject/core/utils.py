import logging

core_logger = logging.getLogger('core_logger')

def some_reusable_function():
    """A sample reusable function."""
    core_logger.info("This is a log from the reusable core module.")
    core_logger.debug("This is a debug log from the core module.")