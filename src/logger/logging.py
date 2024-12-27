import logging
import os 
from datetime import datetime

# Create logs with date and time
LOG_FILE = f"{datetime.now().strftime('%M_%d_%Y_%H_%M_%S')}.log"

# Save logs in logs folder
log_path = os.path.join(os.getcwd(),"logs")

# Create logs folder
os.makedirs(log_path,exist_ok=True)

# Create log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)


# Create message logger
logging.basicConfig(
  filename=LOG_FILEPATH,
  format="[ %(asctime)s ] %(line_number)d %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO
)


logging.info("Logging has started") 

