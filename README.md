# Freevia

A React Native mobile application that can be built into an APK.

## Prerequisites

- Node.js (16 or later)
- Java Development Kit (JDK) 11 or later
- Android SDK
- React Native CLI

## Installation

1. Install dependencies:
```bash
npm install
```

2. For Android development, make sure you have Android SDK installed and ANDROID_HOME environment variable set.

## Building APK

To build the APK file:

```bash
# Build release APK
npm run build-apk
```

The APK will be generated at: `android/app/build/outputs/apk/release/app-release.apk`

## Development

```bash
# Start Metro bundler
npm start

# Run on Android device/emulator
npm run android
```

## Features

- React Native cross-platform app
- Ready-to-build APK configuration
- Modern React Native architecture
- Clean and simple UI