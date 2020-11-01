import os
import unittest
from LoggingLevel import LoggingLevel

class TestLoggingLevel(unittest.TestCase):
    
    def test_error_level_not_in_list_levels(self):
        log = LoggingLevel('AAAA')
        with self.assertRaises(ValueError):
            log.log('Something to log')
    
    def test_add_level(self):
        log = LoggingLevel('EEEE')
        log.add_level('EEEE', 1)
        log.log('Something to log')
    
unittest.main()