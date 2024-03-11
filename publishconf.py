"""
This file is only used if you use `make publish` or
explicitly specify it as your config file.
"""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://justiciadigital.gob.mx"
RELATIVE_URLS = False

# Feeds
FEED_ALL_ATOM = "feeds/atom.xml"
FEED_ALL_RSS = "feeds/rss.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

# Following items are often useful when publishing
DELETE_OUTPUT_DIRECTORY = True

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
