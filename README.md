# LoggingLevel
Simple logging level developed for Sirena Data Analyst Assessment 

### Simple Usage Example
```python
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
var = 12345
log.log('{}'.format(var))

# Creating other logging
other_log = LoggingLevel('DEBUG')
other_log.log('Text from other_log')
```

### Add new levels to logging
The levels are defined in the LoggingLevel.levels variable, they are ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']. To add new levels use:
```python
position_level = 1
log = LoggingLevel('NEW_LEVEL')
log.add_level('NEW_LEVEL', position_level)
```

### Setting current level
```python
log = LoggingLevel()
log.set_level('DEBUG')
```

### Log variables
```python
var = 1234
text = '{}'.format(var)
log = LoggingLevel('WARNING')
log.log(text)
```