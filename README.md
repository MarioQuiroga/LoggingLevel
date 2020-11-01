# LoggingLevel
Simple logging level developed for Sirena Data Analyst Assessment 

### Simple Usage Example
```
import os
from LoggingLevel import LoggingLevel

# Define level environment variable
os.environ['env'] = 'INFO'

# Create object for use
log = LoggingLevel('INFO') # Set current level (default='WARNING')

# Set output file (if not specified, not write in file)
log.set_output_file('output_log.txt')

# Using tool
log.log('Testing log.')
log.log('Testing log.', 'file.py')
log.log('Testing log.', 'file.py', 'function1')

# Creating other logging
other_log = LoggingLevel('DEBUG')
other_log.log('Text from other_log')
```