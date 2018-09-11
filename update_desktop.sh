#!/usr/bin/env bash
# =========================================================================== #
# Description: Automatically change desktop picture
# Author: Michael Fryar

# Get NASA's Astronomy Picture of the Day
python get_apod.py

# Change desktop picture to APOD
osascript <<EOF
tell application "System Events"
    tell every desktop
        set picture to "/Users/mifryar/datasci/apod/apod.jpg"
    end tell
end tell
EOF
