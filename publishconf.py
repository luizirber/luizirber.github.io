#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

# keep the .com address to properly find disqus comments
SITEURL = 'https://blog.luizirber.org'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False

DISQUS_SITENAME = 'gabbleblotchits'

STATIC_PATHS += ['CNAME']
EXTRA_PATH_METADATA.update(
    {'CNAME': {'path': 'CNAME'}},
)
