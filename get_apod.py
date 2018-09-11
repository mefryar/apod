#!/usr/bin/env python
"""Automatically update desktop background.

This module connects to the NASA API to download the Astronomy Picture of the
Day.

It builds on an excellent tutorial by Angela Ambroz:
http://www.angelaambroz.com/blog/posts/2017/Dec/12/automatic_desktop_backgrounds/

"""

import os
import requests
import urllib.request
from datetime import date
from secrets import API_KEY

# Get image url from NASA API
url = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(API_KEY)
r = requests.get(url).json()
image_url = r['url']

# Save image to subfolder
apod_file = "apod.jpg"
urllib.request.urlretrieve(image_url, apod_file)
