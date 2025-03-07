#!/bin/bash

# Start Xvfb
Xvfb :99 -screen 0 1024x768x16 &

# Export the DISPLAY environment variable
export DISPLAY=:99

# Start fluxbox
#fluxbox &

# Run the application
#exec python3.8 run.py
exec $@