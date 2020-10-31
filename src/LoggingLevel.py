import os
class Logging:
  def __init__(self, level: str='LOG'):
    ''' Create Logging Level 
    :level: Set current level
    '''    
    self.level = level
    self.file_output = ''

  def log(self, log:str, file:str='---', func:str='---'):
    ''' Print log if env == curr_level
    :log: message to print
    '''
    env = os.getenv('env', '')
    if self.level == env or env == '':
      text_log = '['+ self.level + '] ['+ file  +'] ['+ func + '] '+ log
      print(text_log)      
      if self.file_output != '':
        with open(file_output, 'a'):
          write(text_log)

  def set_file_output(self, file:str):
    self.file = file

  def set_level(self, level:str):
    self.level = level