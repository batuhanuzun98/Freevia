#!/bin/bash

# Freevia APK Build Script
# This script builds an Android APK from the Python Kivy application

echo "🚀 Starting Freevia APK Build Process..."

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "❌ Buildozer not found. Please install it first:"
    echo "   pip install buildozer"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "main.py" ] || [ ! -f "buildozer.spec" ]; then
    echo "❌ Missing required files (main.py or buildozer.spec)"
    echo "   Please run this script from the project root directory"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Clean previous builds (optional)
echo "🧹 Cleaning previous builds..."
buildozer android clean

# Initialize buildozer (downloads SDK, NDK, etc. - this may take a while)
echo "🔧 Initializing buildozer (this may take a while on first run)..."
buildozer init

# Build the APK in debug mode
echo "📱 Building APK in debug mode..."
buildozer android debug

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ APK build completed successfully!"
    echo "📍 APK location: bin/freevia-0.1-arm64-v8a-debug.apk"
    echo ""
    echo "📋 Next steps:"
    echo "   1. Transfer the APK to your Android device"
    echo "   2. Enable 'Install from unknown sources' in Android settings"
    echo "   3. Install the APK"
    echo ""
    echo "🔧 To build a release APK, run:"
    echo "   buildozer android release"
else
    echo "❌ APK build failed. Check the error messages above."
    exit 1
fi