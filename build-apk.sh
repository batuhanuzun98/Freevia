#!/bin/bash

# Freevia APK Build Script
# This script builds the Android APK for the Freevia app

echo "🚀 Starting Freevia APK build process..."

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: package.json not found. Please run this script from the project root."
    exit 1
fi

# Check if Android directory exists
if [ ! -d "android" ]; then
    echo "❌ Error: Android directory not found."
    exit 1
fi

echo "📱 Building Android APK..."

# Navigate to android directory and build
cd android

# Check if gradlew exists and is executable
if [ ! -x "./gradlew" ]; then
    echo "❌ Error: gradlew not found or not executable."
    exit 1
fi

echo "🔨 Running Gradle build..."
# Build the release APK
./gradlew assembleRelease

if [ $? -eq 0 ]; then
    echo "✅ APK build completed successfully!"
    echo "📱 APK location: android/app/build/outputs/apk/release/"
    
    # List the generated APK files
    if [ -d "app/build/outputs/apk/release/" ]; then
        echo "Generated APK files:"
        ls -la app/build/outputs/apk/release/*.apk 2>/dev/null || echo "APK files will be available after successful build"
    fi
else
    echo "❌ APK build failed. Please check the error messages above."
    exit 1
fi

echo "🎉 Freevia APK build process completed!"
echo ""
echo "To install the APK on your device:"
echo "  adb install android/app/build/outputs/apk/release/app-release.apk"
echo ""
echo "Note: Make sure you have enabled 'Unknown sources' in your device settings."