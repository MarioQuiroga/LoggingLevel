import os
from src.LoggingLevel import *

# Define level environment variable
os.environ['env'] = 'DEBUG'

# Create object for use
log = Logging('DEBUG') # Set current level

# Using the object
log.log('Testing log.')
log.log('Testing log.', 'file.py')
log.log('Testing log.', 'file.py', 'function1')