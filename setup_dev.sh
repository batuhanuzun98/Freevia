#!/bin/bash

# Freevia Development Setup Script
# This script sets up the development environment for Freevia

echo "🚀 Setting up Freevia development environment..."

# Check Python version
python_version=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then
    echo "✅ Python $python_version is compatible (>= 3.8)"
else
    echo "❌ Python $python_version is too old. Please install Python 3.8 or higher."
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Validate project structure
echo "🔍 Validating project structure..."
python validate_structure.py

if [ $? -eq 0 ]; then
    echo "✅ Project structure validation passed"
else
    echo "❌ Project structure validation failed"
    exit 1
fi

echo ""
echo "🎉 Development environment setup complete!"
echo ""
echo "📋 Next steps:"
echo "   1. Run locally: python main.py"
echo "   2. Build APK: ./build_apk.sh"
echo "   3. Or use Docker: docker build -t freevia-builder . && docker run -v \$(pwd):/app freevia-builder"