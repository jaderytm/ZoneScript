# test_zonescript.py
"""
Tests for ZoneScript module.
"""

import unittest
from zonescript import ZoneScript

class TestZoneScript(unittest.TestCase):
    """Test cases for ZoneScript class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZoneScript()
        self.assertIsInstance(instance, ZoneScript)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZoneScript()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
