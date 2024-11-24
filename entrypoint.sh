#!/bin/sh

# Set the DISPLAY environment variable
export DISPLAY=:99

# Start Xvfb
Xvfb -ac :99 -screen 0 1280x1024x16 &

# Execute the CMD
exec "$@"