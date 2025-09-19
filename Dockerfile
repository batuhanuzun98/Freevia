# Dockerfile for building Freevia APK
FROM kivy/buildozer:latest

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Set buildozer home
ENV BUILDOZER_HOME=/buildozer

# Create buildozer directory
RUN mkdir -p $BUILDOZER_HOME

# Build the APK
CMD ["buildozer", "android", "debug"]