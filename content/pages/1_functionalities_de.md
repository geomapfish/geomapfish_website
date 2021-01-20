Title: Funktionalitäten
Date: 2016-10-14
Modified: 2020-03-19
Authors: Michael Kalbermatten, Irene Vontobel, Rémi Bovard
URL: functionalities
Save_as: functionalities.html
Slug: 1_functionalities
Lang: de
<br />
GeoMapFish besteht aus einer Desktop Oberfläche, einer Administrationsschnittstelle, einer API und
einer mobilen Version.

Neben OGC-Standard Geodiensten setzt GMF auch das Mapfish Protokoll ein. Dieses stellt die
effiziente Kommunikation zwischen Client und Server sicher. Auf dieser Basis können
komplexe und leistungsfähige Applikationen gebaut werden.

GeoMapFish kombiniert ein paar der besten OpenSource Tools, die es gibt:

* [OpenLayers](https://openlayers.org/), [AngularJS](https://angularjs.org/) und [ngeo](https://camptocamp.github.io/ngeo/master/apidoc/) für die Client-Seite
* Python Module (vor allem Papyrus, das auf [Pyramid](https://trypyramid.com/) basiert) für die Server-Seite
* [MapFish Print](https://mapfish.github.io/mapfish-print-doc/), ein Java-Servlet für das Drucken von Karteninhalten

## Dokumentation und Support

Die verschiedene GMF Komponenten:

* Die letzte Dokumentation ist [hier](https://camptocamp.github.io/c2cgeoportal/master/)
* Die Server-Seite von GeoMapFish ist [c2cgeoportal](https://github.com/camptocamp/c2cgeoportal/).
* Die Client-Seite von GeoMapFish ist eine Angular Library, die sich [ngeo](https://github.com/camptocamp/ngeo/) nennt.

## GeoMapFish Viewer

### ![Functionalities description]({filename}/images/1_1_responsive.png) Benutzeroberfläche

* Vorlage für Mobile und Desktop Version in "responsive design"

### ![Functionalities description]({filename}/images/1_2_search.png) Volltextsuche

* Dateninhalte
* Layer
* Themen

### ![Functionalities description]({filename}/images/1_3_navigation.png) Navigation

* Zoom & Pan
* Navigationsleiste
* Geolokalisation

### ![Functionalities description]({filename}/images/1_4_query.png) Kartenabfrage

* Punkt und Flächenabfrage
* Resultatfenster als Tabelle oder in einem Popup-Fenster
* Live raster & coordinate interrogation direkte Raster und Koordinatenabfrage

### ![Functionalities description]({filename}/images/1_5_data.png) Daten

* Interne WMS & WMTS
* WMS-T
* Externe Daten (WMS, KML)
* Gliederung in Themen
* Hinzufügen von Layer zu den Themen
* Transparenz und Metadaten
* Dynamische Legende

### ![Functionalities description]({filename}/images/1_6_print.png) Drucken

* PDF & PNG Ausdruck

### ![Functionalities description]({filename}/images/1_7_drawing.png) Zeichnen und Messen

* Punkte
* Linien
* Flächen
* Rechtecke
* Kreise (Azimuth)
* Beschriftung

### ![Functionalities description]({filename}/images/1_8_layer_editing.png) Layer Editieren

* Simple Editiermöglichkeit von Datenbankelementen
* Einfache Konfiguration
* Komplexe Editiermaske (Snapping, Kopieren von Geometrien, Ausschneiden, Löcher extrahieren)

### ![Functionalities description]({filename}/images/1_9_gis.png) GIS Funktionalitäten

* SQL Abfragen und Filter
* Zeit-Schieberegler

### ![Functionalities description]({filename}/images/1_10_misc.png) Weiteres

* Profile
* Google StreetView Integration
* Permalink
* Verkürzte Permalink-URL

---

## GeoMapFish Administration

### ![Functionalities description]({filename}/images/2_1_configuration.png) Datenadministration

* Layer Konfiguration
* Layergruppe Konfiguration
* Themen Konfiguration
* DatanquelleKonfiguration

### ![Functionalities description]({filename}/images/2_2_authentication.png) Authentifizierung

* LDAP, NTLM & other interactions

### ![Functionalities description]({filename}/images/2_3_roles.png) Rollen

* Konfiguration der Rollen
* Konfiguration der Benutzer
* Konfiguration von Flächenbeschränkungen
* Konfiguration von benutzergebundenen Funktionalitäten

---

## GeoMapFish server

### ![Functionalities description]({filename}/images/3_1_pdf.png) PDF Reports

### ![Functionalities description]({filename}/images/3_2_webmapping.png) Webmapping backends

* MapServer
* QGIS Server
* ArcGIS for Server

### ![Functionalities description]({filename}/images/3_3_docker.png) Docker deployment

<br /><br />
Für einen besseren Überblick, gehen Sie bitte auf die [feature Seite](https://github.com/camptocamp/ngeo/blob/master/docs/features.md).
