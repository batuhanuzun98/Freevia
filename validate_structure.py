#!/usr/bin/env python3
"""
Validate the structure of the Freevia project without running Kivy
"""

import os
import ast
import sys

def validate_file_exists(filename):
    """Check if a file exists"""
    if os.path.exists(filename):
        print(f"✅ {filename} exists")
        return True
    else:
        print(f"❌ {filename} missing")
        return False

def validate_python_syntax(filename):
    """Validate Python file syntax"""
    try:
        with open(filename, 'r') as f:
            source = f.read()
        ast.parse(source)
        print(f"✅ {filename} has valid Python syntax")
        return True
    except SyntaxError as e:
        print(f"❌ {filename} has syntax error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading {filename}: {e}")
        return False

def validate_imports(filename):
    """Check if required imports are present in Python file"""
    try:
        with open(filename, 'r') as f:
            source = f.read()
        
        required_imports = [
            'from kivy.app import App',
            'from kivy.uix.boxlayout import BoxLayout',
            'from kivy.uix.label import Label',
            'from kivy.uix.button import Button'
        ]
        
        missing_imports = []
        for imp in required_imports:
            if imp not in source:
                missing_imports.append(imp)
        
        if missing_imports:
            print(f"❌ {filename} missing imports: {missing_imports}")
            return False
        else:
            print(f"✅ {filename} has all required imports")
            return True
            
    except Exception as e:
        print(f"❌ Error checking imports in {filename}: {e}")
        return False

def main():
    """Main validation function"""
    print("🔍 Validating Freevia project structure...")
    print()
    
    all_valid = True
    
    # Check required files
    required_files = [
        'main.py',
        'requirements.txt',
        'buildozer.spec',
        'build_apk.sh',
        'README.md',
        '.gitignore'
    ]
    
    for file in required_files:
        if not validate_file_exists(file):
            all_valid = False
    
    print()
    
    # Validate Python syntax
    python_files = ['main.py']
    for file in python_files:
        if os.path.exists(file):
            if not validate_python_syntax(file):
                all_valid = False
    
    print()
    
    # Validate imports
    if os.path.exists('main.py'):
        if not validate_imports('main.py'):
            all_valid = False
    
    print()
    
    # Check build script permissions
    if os.path.exists('build_apk.sh'):
        if os.access('build_apk.sh', os.X_OK):
            print("✅ build_apk.sh is executable")
        else:
            print("❌ build_apk.sh is not executable")
            all_valid = False
    
    print()
    
    if all_valid:
        print("🎉 All validations passed! Project structure is correct.")
        print("📱 Ready to build APK with: ./build_apk.sh")
    else:
        print("❌ Some validations failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == '__main__':
    main()