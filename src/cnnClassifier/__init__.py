import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 
"""
%(asctime)s: Represents the timestamp of the log message in a human-readable format. %s represents a string placeholder, and asctime stands for "asctime" (which means "as string time").
%(levelname)s: Represents the logging level of the message (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL). levelname is a placeholder for the logging level. In our case level->info
%(module)s: Represents the name of the Python module where the logging call was made. module is a placeholder for the module name.
%(message)s: Represents the actual log message. message is a placeholder for the log message itself."""



log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")