#!/bin/bash

Xvfb $DISPLAY -nolisten inet6 -nolisten tcp -nolisten unix -screen 0 1920x1280x24 +extension RANDR >/dev/null 2>&1 &

for i in 1 2 3 4 5; do xdpyinfo -display $DISPLAY >/dev/null 2>&1 && break || sleep '1s'; done

xdpyinfo -display $DISPLAY >/dev/null 2>&1 && echo 'In use' || echo 'Free'

# echo "here"

/lambda-entrypoint.sh "$1"