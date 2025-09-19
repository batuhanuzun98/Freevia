# Freevia

A simple Python mobile application built with Kivy that can be compiled to Android APK.

## 📱 About

Freevia is a demonstration of how to create Android APK files from Python code using the Kivy framework and Buildozer. The app features a simple interface where users can enter their name and receive a personalized greeting.

## 🚀 Features

- Simple and intuitive user interface
- Cross-platform (runs on desktop and Android)
- Built with Kivy for native mobile performance
- Easy APK generation with Buildozer

## 📋 Prerequisites

### For Local Development:
- Python 3.8 or higher
- pip (Python package manager)

### For APK Building:
- Linux or macOS (Windows users should use WSL or Docker)
- Java Development Kit (JDK) 8 or 11
- Android SDK (will be downloaded automatically by Buildozer)
- Git

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/batuhanuzun98/Freevia.git
cd Freevia
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App Locally (Desktop)
```bash
python main.py
```

## 📱 Building APK

### Method 1: Using the Build Script (Recommended)
```bash
./build_apk.sh
```

### Method 2: Manual Build
```bash
# Initialize buildozer (first time only)
buildozer init

# Build debug APK
buildozer android debug

# Build release APK (for production)
buildozer android release
```

### Method 3: Using Docker
```bash
# Build the Docker image
docker build -t freevia-builder .

# Run the container to build APK
docker run -v $(pwd):/app freevia-builder
```

## 📦 APK Location

After successful build, the APK will be located at:
- Debug APK: `bin/freevia-0.1-arm64-v8a-debug.apk`
- Release APK: `bin/freevia-0.1-arm64-v8a-release.apk`

## 📋 Installation on Android

1. Transfer the APK file to your Android device
2. Enable "Install from unknown sources" in Android settings:
   - Go to Settings > Security > Unknown sources (Android < 8.0)
   - Go to Settings > Apps > Special access > Install unknown apps (Android 8.0+)
3. Open the APK file and follow installation prompts

## 🔧 Customization

### Modify the App
Edit `main.py` to customize the application behavior and UI.

### Change App Configuration
Edit `buildozer.spec` to modify:
- App name and package information
- Icons and splash screens
- Permissions
- Target Android versions
- Build architectures

### Add Dependencies
Add Python packages to `requirements.txt` and update the `requirements` line in `buildozer.spec`.

## 🐛 Troubleshooting

### Common Issues:

1. **Build fails with SDK/NDK errors:**
   ```bash
   buildozer android clean
   rm -rf .buildozer
   buildozer android debug
   ```

2. **Permission denied on build script:**
   ```bash
   chmod +x build_apk.sh
   ```

3. **Java version issues:**
   Ensure you have JDK 8 or 11 installed:
   ```bash
   java -version
   ```

4. **Out of space during build:**
   The first build downloads ~2GB of Android SDK/NDK. Ensure sufficient disk space.

### Build Logs
Check build logs in `.buildozer/logs/` for detailed error information.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

If you encounter issues or have questions:
1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed information

## 🔗 Resources

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Android Development](https://developer.android.com/)