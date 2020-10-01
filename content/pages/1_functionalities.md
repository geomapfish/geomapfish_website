Title: Functionalities
Date: 2016-10-14
Modified: 2020-03-19
Author: Michael Kalbermatten, Rémi Bovard
URL: functionalities
Save_as: functionalities.html
Slug: 1_functionalities
Lang: en
Tags: Geoportal, Open Source, GeoMapFish, GIS, Geospatial
Summary: GeoMapFish is an application with a responsive ergonomics and a wide choice of functionalites
<br />
GeoMapFish is composed of a desktop WebGIS interface, an administration interface, an API for map integration
in thirdparty websites and a mobile version.

Besides the OGC-Standard web services, a MapFish protocol adapted to the efficient communication
between Client and Server is available. On this basis, complex and high performance web mapping 
applications can be built.

GeoMapFish combines some of the best Open Source tools in one application:

* [OpenLayers](https://openlayers.org/), [AngularJS](https://angularjs.org/) and [ngeo](https://camptocamp.github.io/ngeo/master/apidoc/) on the client side
* Python modules (especially Papyrus based on [Pyramid](https://trypyramid.com/)) on the server side
* [MapFish Print](https://mapfish.github.io/mapfish-print-doc/), a Java servlet dedicated to print geographic documents

## Documentation and support

Read the documentation:

* Latest documentation is available [here](https://camptocamp.github.io/c2cgeoportal/master/)
* The server part of GeoMapFish is [c2cgeoportal](https://github.com/camptocamp/c2cgeoportal/).
* The client part of GeoMapFish is an Angular library called [ngeo](https://github.com/camptocamp/ngeo/).

## GeoMapFish Viewer

### ![Functionalities description]({filename}/images/1_1_responsive.png) User interface

* Desktop & mobile responsive templates

### ![Functionalities description]({filename}/images/1_2_search.png) Full text search

* Data
* Layers
* Themes

### ![Functionalities description]({filename}/images/1_3_navigation.png) Navigation

* Zoom & pan
* Navigation bar
* Geolocation

### ![Functionalities description]({filename}/images/1_4_query.png) Query

* Point & rectangular interrogation
* Table and/or popup results
* Live raster & coordinate interrogation

### ![Functionalities description]({filename}/images/1_5_data.png) Data

* Internal WMS & WMTS
* WMS-T
* External data (WMS, KML)
* Organisation into themes
* Layer adding in themes
* Transparency & metadata
* Dynamic legend

### ![Functionalities description]({filename}/images/1_6_print.png) Print

* PDF & PNG print

### ![Functionalities description]({filename}/images/1_7_drawing.png) Drawing & measure

* Points
* Lines
* Surfaces
* Rectangles
* Circles (azimuth)
* Labels

### ![Functionalities description]({filename}/images/1_8_layer_editing.png) Layer editing

* Simple DB editing
* Simple configuration
* Complex editing (snapping, copying, cutting, donut extractor)

### ![Functionalities description]({filename}/images/1_9_gis.png) GIS functionalities

* SQL queries & filters
* Time sliders

### ![Functionalities description]({filename}/images/1_10_misc.png) Misc

* Profile
* Google StreetView integration
* Permalink
* Permalink shortener

---

## GeoMapFish administration

### ![Functionalities description]({filename}/images/2_1_configuration.png) Data administration

* Layer configuration
* Group configuration
* Theme configuration
* Data source configuration

### ![Functionalities description]({filename}/images/2_2_authentication.png) Authentication

* LDAP, NTLM & other interactions

### ![Functionalities description]({filename}/images/2_3_roles.png) Roles

* Roles configuration
* User configuration
* User restriction areas
* User functionalites

---

## GeoMapFish server

### ![Functionalities description]({filename}/images/3_1_pdf.png) PDF reporting

### ![Functionalities description]({filename}/images/3_2_webmapping.png) Webmapping backends

* MapServer
* QGIS Server
* ArcGIS for Server

### ![Functionalities description]({filename}/images/3_3_docker.png) Docker deployment

<br /><br />
For a better overview between features and versions, please refer to the [feature page](https://github.com/camptocamp/ngeo/blob/master/docs/features.md).

---

## Others

### QGIS GeoMapFish Locator Plugin

* [GeoMapFish Locator](https://plugins.qgis.org/plugins/geomapfish_locator/): use GeoMapFish full text search service in QGIS.
