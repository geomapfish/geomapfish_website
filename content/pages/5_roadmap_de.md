Title: Roadmap
Date: 2017-06-20
Modified: 2021-06-10
Author: Michael Kalbermatten, Rémi Bovard, Irene Vontobel
URL: roadmap
Save_as: roadmap.html
Slug: 5_roadmap
Lang: de
Tags: Geoportal, Open Source, GeoMapFish, GIS, Geospatial
Summary: GeoMapFish ist eine Open-Source Plattform, die sich mit jeder Version weiterentwickelt, indem sie viele neue Funktionalitäten bietet

<br />
Hier unten finden Sie die Roadmap von GeoMapFish, aber auch die Links zu den Release Notes der verschiedenen Versionen.

Letztes Update der Seite: **10.06.2021**

Für eine komplette Roadmap bis 2024, sehen dieser Dokument: [GMF_2024_Roadmap.pdf](/documents/meetings/2021-06-08/GMF_2024_Roadmap.pdf)

## Version Snook (2.7 LTR)

Nächste Version.

* Entwicklungen: **Anfang September 2021**
* Geschätztes Freigabedatum: **Summer 2022**

Diese Version habe keine neuen funktionalitäten. Es ist nur eine technische Migration, und das Ziel ist GeoMapFish ohne AngularJS zu bereiten, weil AngularJs ist nicht mehr seit ende 2021 unterstützt.

### Technische Veränderungen

* Überprüfung der neuen technischen Auswahlen mit einem POC.
* Fusionieren client parts von Ngeo/GMF.
* Auswechseln AngularJs state-management mit RxJS.
* Auswechseln AngularJs internationalization stack mit i18next.
* Integrieren litelement and lithtml zu der Austauch von AngularJS bereiten.
* Unterstützung Standard Web Components.

<hr />

## Version 2.6

Version in der Entwicklungsphase:

* Entwicklungen: **Anfang Juli 2020**
* Geschätztes Freigabedatum: **Frühjahr 2021**
* Dokumentation: laufend [camptocamp.github.io/c2cgeoportal/master](https://camptocamp.github.io/c2cgeoportal/master/)

### Funktionalitäten

#### Interface

* [2.6.24] Push a message to user when server authentication is lost
* [2.6.32] Right panel resizable for all tools

#### Query

* [2.6.10] CSV export in Window
* [2.6.46] Define a per layer click tolerance
* [2.6.53] Scale limit on WMTS query

#### Search

* [2.6.26] Possiblitiy to add keywords to layers in order to find them easier
* [2.6.27] Full-text-search for layers

#### Print

* [2.6.29] Handle case with layers with a legend too big to show on one A4 sheet

#### Permalink

* [2.6.25] See the configuration of the timeslider/timepicker before sharing

#### Measure and redlining

* [2.6.1] Draw an arrow
* [2.6.31] Snapping functionality for measuring and drawing tools

#### Editing

* [2.6.20] Check data type and display warning before saving
* [2.6.22] Add a column named "order", in order to sort dropdown lists
* [2.6.51] Allow editing of overlayed geometries (editing and redlining)

#### External data

* [2.6.34] Display legend of imported WMS layers
* [2.6.35] Interrogation of external WMS with GetFeatureInfo
* [2.6.47] Drag & drop files to show them on map

<hr />

## Version 2.5

* Freigabedatum: **23. April 2020**
* EOS: **Oktober 2021**
* Dokumentation: [camptocamp.github.io/c2cgeoportal/2.5](https://camptocamp.github.io/c2cgeoportal/2.5/)

### Funktionalitäten

1. Verbesserung vom WMS browser (Layer Suche, Server Liste)
2. Map slider (zwei Karten vergleichen)
3. Verbesserung der Zeichenwerkzeuge (Länge, Grösse)
4. Legende automatisch schliessen, wenn den Layer deaktiviert wird
5. Snap Layers anzeigen und aktivieren / deaktivieren lassen
6. Intranet Benutzerpanel
7. Anzeige und Validierung von obligatorischen Feldern im Editionsformular
8. Verbesserung der Zeitleiste (dynamisches Karten Rendering)
9. Definition von min und max Kartenmassstab von WMTS Layers
10. Filter aktiv lassen selbst wenn Formular geschlossen wird
11. Abfrage mit Polygon
12. Globales Laden und Zähleranzeige
13. Verkürzung langer Namen im Anzeigefenster
14. Story maps
15. KML Styling (Import & Export)
16. Benützen der Desktopversion auf einem Tablet
17. Geolocation auf der Desktopversion
18. WMS GetFeatureInfo auf nicht WFS Servern
19. Sicherheit - Kein Caching von Zugangsdaten
20. Sicherheit - Konfigurierbare Kontosperrung
21. Sicherheit - Verschlüsselte Passwordspeicherung
22. Sicherheit - Session timeouts
23. Architektur - Docker only

<hr />

## Version 2.4 (LTR)

* Freigabedatum: **7. Juli 2019**
* EOS: **Juli 2022**
* Dokumentation: [camptocamp.github.io/c2cgeoportal/2.4](https://camptocamp.github.io/c2cgeoportal/2.4/)

### Funktionalitäten

1. IFRAME Integration
2. Editieren - Kolonne Reihenfolge
3. Editieren - Read only attributes
4. Editieren - Link zu einem external Formular
5. Zeichnen - Delete vertex menu
6. Zeichnen - Zoom beim Recenter
7. Read only Zeichnungen im Mobile
8. Layer tree - Resize Panel
9. Layer tree - Radio Buttons
10. Query - Auto-links in den Resultaten
11. Interface - App loading widget
12. Interface - Title von den ersten Panel
13. A0 ausdrucken

<hr />

## Version 2.3

* Freigabedatum: **23. Mai 2018**
* Dokumentation: [camptocamp.github.io/c2cgeoportal/2.3](https://camptocamp.github.io/c2cgeoportal/2.3/)

### Funktionalitäten

1. Integration des WMS / KML Browser + Permalink
2. Rotation der Karte
3. Popup-Fenster auf der Karte verschieben und skalieren
4. Anpassung Administrationsoberfläche
5. Optimierung des Resultatefensters
6. Flush / no flush vom Layertree in der mobilen Version
7. Transparenz der Layer in der mobilen Version

<hr />

## Version 2.2

* Freigabedatum: **22. Januar 2018**
* Dokumentation: [camptocamp.github.io/c2cgeoportal/2.2](https://camptocamp.github.io/c2cgeoportal/2.2/)

### Funktionalitäten

1. erweiterte Attributabfrage und Filter
2. Berücksichtigung der Zeit bei Attributabfragen
3. "Es konnte nichts gefunden werden" Hinweistext bei leerer Suche
4. Integration des Street View Plugins
5. "Alles löschen" Button im Layertree
6. benutzerdefinierter Druckmassstab beim Drucken
7. Android Webrowser Kompatibilität
8. Definierte Standard-Transparenz von WMS / WMTS Ebenen
