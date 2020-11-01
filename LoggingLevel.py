import os
import datetime

class LoggingLevel:
  levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

  def __init__(self, level: str='WARNING'):
    ''' Create Logging Level.
    :level: Set current level.
    '''    
    self.level = level
    self.file_output = ''

  def log(self, string:str, file:str='---', func:str='---'):
    ''' Print log if env == level.
    :string: message to print.
    :file: Optional log file where the event occurs.
    :func: Optional log function where the event occurs.
    '''
    # Check env var
    env = 'WARNING'
    if os.getenv('env', '')!='':
      env = os.getenv('env', 'WARNING')
    
    # Perform log
    i_env = LoggingLevel.levels.index(env)
    i_lev = LoggingLevel.levels.index(self.level)
    if i_lev>=i_env:
      timestamp =  str(datetime.datetime.now())
      text_log = '['+ timestamp[:19] + '] ['+ self.level + '] ['+ file  +'] ['+ func + '] '+ string
      print(text_log)      
      if self.file_output != '':
        with open(self.file_output, 'a') as f:
          f.write(text_log+'\n')

  def set_output_file(self, file:str):
    ''' If it was not configured, the log will not be saved in a file.
    :file: Path to output file.
    '''
    self.file_output = file

  def set_level(self, level:str):
    ''' Change current level.
    :level: any text can be used. If not in Logging.levels, ValueError exception raised in logging.
    '''    
    self.level = level

  def add_level(self, new_level:str, position:int=0):
    ''' Add level to list levels in the given position.
    :new_level: Level to add.
    :position: If not specified add first position.
    '''
    LoggingLevel.levels.insert(position, new_level)
