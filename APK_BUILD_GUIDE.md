# Freevia APK Build Guide

This guide explains how to convert the Freevia app to an APK file.

## Prerequisites

Before building the APK, ensure you have the following installed:

1. **Node.js** (version 16 or later)
2. **Java Development Kit (JDK)** (version 11 or later)
3. **Android SDK** with the following components:
   - Android SDK Platform 33
   - Android SDK Build-Tools 33.0.0
   - Android SDK Platform-Tools
4. **Android NDK** (version 23.1.7779620)

## Environment Setup

1. Set the `ANDROID_HOME` environment variable:
   ```bash
   export ANDROID_HOME=/path/to/android-sdk
   export PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools
   ```

2. Install project dependencies:
   ```bash
   npm install
   ```

## APK Build Methods

### Method 1: Using npm script (Recommended)
```bash
npm run build-apk
```

### Method 2: Using the build script
```bash
./build-apk.sh
```

### Method 3: Manual Gradle build
```bash
cd android
./gradlew assembleRelease
```

## APK Output Location

After a successful build, the APK will be located at:
```
android/app/build/outputs/apk/release/app-release.apk
```

## Installing the APK

### On Device via ADB
```bash
adb install android/app/build/outputs/apk/release/app-release.apk
```

### Manual Installation
1. Transfer the APK file to your Android device
2. Enable "Install from Unknown Sources" in device settings
3. Tap the APK file to install

## Build Variants

- **Debug**: `./gradlew assembleDebug` - For testing and development
- **Release**: `./gradlew assembleRelease` - For production distribution

## Troubleshooting

### Common Issues

1. **Gradle build fails**: Ensure Java 11+ is installed and JAVA_HOME is set
2. **SDK not found**: Set ANDROID_HOME environment variable correctly
3. **Build tools not found**: Install required Android SDK components

### Build Optimization

For smaller APK size, you can enable ProGuard by setting:
```gradle
def enableProguardInReleaseBuilds = true
```
in `android/app/build.gradle`

## App Signing

The current setup uses a debug keystore for signing. For production:

1. Generate a release keystore:
   ```bash
   keytool -genkey -v -keystore release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
   ```

2. Update `android/app/build.gradle` with release signing configuration

## Features Included

- ✅ React Native 0.72.6
- ✅ Android API Level 33 support
- ✅ ARM64, ARMv7, x86, x86_64 architectures
- ✅ Hermes JavaScript engine
- ✅ Debug keystore for development
- ✅ Material Design components
- ✅ Ready-to-build configuration

## Next Steps

1. Install dependencies: `npm install`
2. Build APK: `npm run build-apk`
3. Install on device: `adb install android/app/build/outputs/apk/release/app-release.apk`

The Freevia app is now ready to be converted to APK format! 📱