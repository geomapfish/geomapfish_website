#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'GeoMapFish user community'
SITENAME = u'GeoMapFish'
SITEURL = ''

SITELOGO = 'images/brand/logo.png'
FAVICON = 'images/brand/favicon.ico'

GITHUB_URL = 'http://github.com/camptocamp/c2cgeoportal'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

PAGE_ORDER_BY = 'basename'

PAGES_SORT_ATTRIBUTE = 'slug'

STATIC_PATHS = ['images', 'documents']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

I18N_SUBSITES = {
    'fr': {
        'SITELOGO': '../images/brand/logo.png',
        'FAVICON': '../images/brand/favicon.ico'
    },
    'de': {
        'SITELOGO': '../images/brand/logo.png',
        'FAVICON': '../images/brand/favicon.ico'
    }
}

THEME = 'themes'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

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
SOCIAL = (
    ('Google Group', 'https://groups.google.com/forum/#!forum/geomapfish', 'google-plus'),
    ('Twitter', 'https://twitter.com/GeoMapFish'),
    ('GitHub', GITHUB_URL)
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
