import os
class Logging:
  def __init__(self, level: str='LOG'):
    ''' Create Logging Level .
    :level: Set current level.
    '''    
    self.level = level
    self.file_output = ''

  def log(self, string:str, file:str='---', func:str='---'):
    ''' Print log if env == level.
    :string: message to print.
    '''
    env = os.getenv('env', '')
    if self.level == env or env == '':
      text_log = '['+ self.level + '] ['+ file  +'] ['+ func + '] '+ string
      print(text_log)      
      if self.file_output != '':
        with open(self.file_output, 'a') as f:
          f.write(text_log+'\n')

  def set_output_file(self, file:str):
    ''' If it was not configured, the log will not be saved in a file
    '''
    self.file_output = file

  def set_level(self, level:str):
    ''' Change current level.
    :level: any text can be used. 
    '''
    self.level = level