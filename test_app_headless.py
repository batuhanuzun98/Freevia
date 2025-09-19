#!/usr/bin/env python3
"""
Headless unit tests for Freevia application
"""

import unittest
import sys
import os

# Set environment variable to prevent Kivy from trying to create a window
os.environ['KIVY_UNITTEST'] = '1'

# Add the current directory to the path to import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class TestFreeviaAppStructure(unittest.TestCase):
    """Test the structure of the Freevia application without instantiating UI"""
    
    def test_import_main_module(self):
        """Test that we can import the main module"""
        try:
            import main
            self.assertTrue(hasattr(main, 'FreeviaApp'))
        except ImportError as e:
            self.fail(f"Failed to import main module: {e}")
    
    def test_freevia_app_class_exists(self):
        """Test that FreeviaApp class exists and has required methods"""
        import main
        
        # Check class exists
        self.assertTrue(hasattr(main, 'FreeviaApp'))
        
        # Check it's a class
        self.assertTrue(isinstance(main.FreeviaApp, type))
        
        # Check required methods exist
        self.assertTrue(hasattr(main.FreeviaApp, 'build'))
        self.assertTrue(hasattr(main.FreeviaApp, 'on_button_press'))
    
    def test_module_structure(self):
        """Test the overall module structure"""
        import main
        
        # Check if main module can be executed
        self.assertTrue(hasattr(main, '__name__'))
        
        # Check for expected imports
        import inspect
        source = inspect.getsource(main)
        
        # Check for essential Kivy imports
        self.assertIn('from kivy.app import App', source)
        self.assertIn('from kivy.uix.boxlayout import BoxLayout', source)
        self.assertIn('from kivy.uix.label import Label', source)
        self.assertIn('from kivy.uix.button import Button', source)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)