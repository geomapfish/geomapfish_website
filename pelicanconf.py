#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Geomapfish user community'
SITENAME = u'Geomapfish'
SITEURL = ''

GITHUB_URL = 'http://github.com/camptocamp/c2cgeoportal'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

PAGE_ORDER_BY = 'basename'

STATIC_PATHS = ['images']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

I18N_SUBSITES = {
    'fr': {
        #'SITENAME': 'Hezkej coucou',
     },
     'de':{}
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Google Group', 'https://groups.google.com/forum/#!forum/geomapfish'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
