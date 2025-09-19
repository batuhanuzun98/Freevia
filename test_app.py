#!/usr/bin/env python3
"""
Unit tests for Freevia application
"""

import unittest
import sys
import os

# Add the current directory to the path to import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import FreeviaApp


class TestFreeviaApp(unittest.TestCase):
    """Test cases for the Freevia application"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.app = FreeviaApp()
    
    def test_app_creation(self):
        """Test that the app can be created"""
        self.assertIsInstance(self.app, FreeviaApp)
        self.assertEqual(self.app.__class__.__name__, 'FreeviaApp')
    
    def test_app_build_method_exists(self):
        """Test that the build method exists"""
        self.assertTrue(hasattr(self.app, 'build'))
        self.assertTrue(callable(getattr(self.app, 'build')))
    
    def test_button_handler_exists(self):
        """Test that the button handler method exists"""
        self.assertTrue(hasattr(self.app, 'on_button_press'))
        self.assertTrue(callable(getattr(self.app, 'on_button_press')))
    
    def test_app_title(self):
        """Test app title configuration"""
        # The title should be accessible via the class name
        self.assertEqual(self.app.__class__.__name__, 'FreeviaApp')


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)