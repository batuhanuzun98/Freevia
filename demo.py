#!/usr/bin/env python3
"""
Demonstration script showing the Freevia project is ready for APK generation
"""

import os
import sys

def check_project_status():
    """Check the status of the Freevia project"""
    print("🎯 Freevia APK Project Status Check")
    print("=" * 50)
    print()
    
    # Check required files
    required_files = {
        'main.py': 'Main Kivy application',
        'buildozer.spec': 'Android build configuration',
        'requirements.txt': 'Python dependencies',
        'build_apk.sh': 'APK build script',
        'setup_dev.sh': 'Development setup script',
        'Dockerfile': 'Containerized build environment',
        'README.md': 'Complete documentation',
        '.gitignore': 'Build artifacts exclusion'
    }
    
    all_files_present = True
    
    print("📁 Required Files:")
    for filename, description in required_files.items():
        if os.path.exists(filename):
            print(f"   ✅ {filename:<20} - {description}")
        else:
            print(f"   ❌ {filename:<20} - {description} (MISSING)")
            all_files_present = False
    
    print()
    
    # Check build tools
    print("🔧 Build Tools Status:")
    
    # Check if buildozer is available
    if os.system("which buildozer > /dev/null 2>&1") == 0:
        print("   ✅ Buildozer installed")
    else:
        print("   ❌ Buildozer not installed (run: pip install buildozer)")
    
    # Check if Python version is adequate
    python_version = sys.version_info
    if python_version >= (3, 8):
        print(f"   ✅ Python {python_version.major}.{python_version.minor} (>= 3.8)")
    else:
        print(f"   ❌ Python {python_version.major}.{python_version.minor} (< 3.8 - upgrade needed)")
    
    print()
    
    # Show next steps
    print("🚀 Next Steps to Build APK:")
    print("   1. Install dependencies: ./setup_dev.sh")
    print("   2. Build APK: ./build_apk.sh")
    print("   3. Or use Docker: docker build -t freevia . && docker run -v $(pwd):/app freevia")
    print()
    
    print("📱 APK will be generated in: bin/freevia-0.1-arm64-v8a-debug.apk")
    print()
    
    # Show app features
    print("✨ App Features:")
    print("   • Simple mobile-friendly interface")
    print("   • User input and personalized greetings")
    print("   • Built with Kivy for cross-platform support")
    print("   • Ready for Android deployment")
    print()
    
    if all_files_present:
        print("🎉 PROJECT STATUS: READY FOR APK GENERATION!")
    else:
        print("❌ PROJECT STATUS: MISSING FILES - CHECK ABOVE")
        
    return all_files_present

if __name__ == '__main__':
    success = check_project_status()
    sys.exit(0 if success else 1)