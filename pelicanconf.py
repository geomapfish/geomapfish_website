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
        'FAVICON': '../images/brand/favicon.ico',
        'SIDEBAR_IMAGES_HEADER': 'Références'
    },
    'de': {
        'SITELOGO': '../images/brand/logo.png',
        'FAVICON': '../images/brand/favicon.ico',
        'SIDEBAR_IMAGES_HEADER': 'Referenzen'
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
    [
        '/images/references/aprona.png',
        'https://carto.aprona.net',
        "Aprona, l'observatoire de la nappe d'Alsace"
    ],
    [
        '/images/references/cartoriviera.png',
        'https://map.cartoriviera.ch',
        "Géoportail cartographique de la Riviera"
    ],
    [
        '/images/references/cartolacote.png',
        'https://map.cartolacote.ch',
        "Géoportail Cartolacôte"
    ],
    [
        '/images/references/cjl.png',
        'https://map.cjl.ch',
        "Géoportail du district de Morges"
    ],
    [
        '/images/references/saint-pierre.png',
        'https://geo.saintpierre.re',
        "Géoportail de Saint-Pierre"
    ],
    [
        '/images/references/jura.svg',
        'https://geo.jura.ch',
        "Géoportail du Système d'Information du Territoire Jurassien"
    ],
    [
        '/images/references/neuchatel.png',
        'https://sitn.ne.ch',
        "Géoportail du Système d'Information du Territoire Neuchâtelois"
    ],
    [
        '/images/references/epfl.svg',
        'https://geoportail.epfl.ch',
        "Géoportail EPFL"
    ],
    [
        '/images/references/mapnv.png',
        'https://mapnv.ch',
        "Géoportail Nord Vaudois - Yverdon-les-Bains"
    ],
    [
        '/images/references/ticino.png',
        'https://map.geo.ti.ch',
        "Geoportale del Cantone Ticino"
    ],
    [
        '/images/references/basel-land.svg',
        'https://geoview.bl.ch',
        "Geoview Basel Landschaft"
    ],
    [
        '/images/references/graubunden.png',
        'https://map.geo.gr.ch',
        "Graubünden Interaktive Karten"
    ],
    [
        '/images/references/nendaz.png',
        'https://nendaz-geoportail.sig.cloud.camptocamp.net',
        "Guichet cartographique de Nendaz"
    ],
    [
        '/images/references/mapbs.png',
        'https://map.geo.bs.ch',
        "MapBS Geoportal Kanton Basel-Stadt"
    ],
    [
        '/images/references/grand-chatellerault.png',
        'https://carto.grand-chatellerault.fr',
        "Portail Cartographique de l'Agglomération du Pays Châtelleraudais"
    ],
    [
        '/images/references/sigip.png',
        'https://www.sigip.ch',
        "Système d'Information Géographique Intercommunal de Pully et Belmont"
    ],
    [
        '/images/references/vsgis.png',
        'https://www.vsgis.ch',
        "WebGIS der Walliser Gemeinden von RUDAZ+PARTNER SA/AG"
    ],
    [
        '/images/references/kantonschwyz.png',
        'https://map.geo.sz.ch',
        "WebGIS Kanton Schwyz"
    ],
    [
        '/images/references/geocommunes.png',
        'http://www.geocommunes.ch/references/',
        "Association GeoCommunes"
        
    ]
]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
