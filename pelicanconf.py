#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'GeoMapFish user community'
SITENAME = u'GeoMapFish'
SITEURL = ''

SITELOGO = 'images/brand/logo.png'
FAVICON = 'images/brand/favicon.ico'

GITHUB_URL = 'https://github.com/camptocamp/geomapfish'

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
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISABLE_SIDEBAR_TITLE_ICONS = True
SIDEBAR_IMAGES_HEADER = 'References'
SIDEBAR_IMAGES = [
    (
        'images/references/cartoriviera.png',
        'https://map.cartoriviera.ch'
    ),
    (
        'images/references/cjl.png',
        'https://map.cjl.ch'
    ),
    (
        'images/references/saint-pierre.png',
        'https://geo.saintpierre.re'
    ),
    (
        'images/references/jura.svg',
        'https://geo.jura.ch'
    ),
    (
        'images/references/neuchatel.png',
        'https://sitn.ne.ch'
    ),
    (
        'images/references/epfl.svg',
        'https://geoportail.epfl.ch'
    ),
    (
        'images/references/mapnv.png',
        'https://mapnv.ch'
    ),
    (
        'images/references/ticino.png',
        'https://map.geo.ti.ch'
    ),
    (
        'images/references/basel-land.svg',
        'https://geoview.bl.ch'
    ),
    (
        'images/references/graubunden.png',
        'https://map.geo.gr.ch'
    ),
    (
        'images/references/nendaz.png',
        'https://nendaz-geoportail.sig.cloud.camptocamp.net'
    ),
    (
        'images/references/mapbs.png',
        'https://map.geo.bs.ch'
    ),
    (
        'images/references/grand-chatellerault.png',
        'https://carto.grand-chatellerault.fr'
    ),
    (
        'images/references/sigip.png',
        'https://www.sigip.ch'
    ),
    (
        'images/references/vsgis.png',
        'https://www.vsgis.ch'
    ),
    (
        'images/references/kantonschwyz.png',
        'https://map.geo.sz.ch'
    )
]
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
