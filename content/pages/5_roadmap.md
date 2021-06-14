Title: Roadmap
Date: 2017-06-20
Modified: 2020-09-23
Authors: Michael Kalbermatten, Rémi Bovard
URL: roadmap
Save_as: roadmap.html
Slug: 5_roadmap
Lang: en
<br />
Here under you will find the GeomapFish roadmap and the functionalities changelog.

Latest page update: **2020-09-23**

For a complete Roadmap until 2024, please see this document: [GMF_2024_Roadmap.pdf](/documents/meetings/2021-06-08/GMF_2024_Roadmap.pdf)

## Version 2.7 (LTR)

Next Version.

* Development: **Starting in September 2021**
* Estimated release date: **Summer 2022**

This Version won't have any new business functionality. It will be a pure technical migration, and has as main objective to prepare GeoMapFish for the removal of AngularJS, which will reach it's end of life at the end of 2021.

### Technical changes

* Validate new technological choices with a POC.
* Merge Ngeo/GMF client parts.
* Replace AngularJs state-management with RxJS.
* Replace AngularJs internationalization stack with i18next.
* Integrate litelement and lithtml to prepare the replacement of AngularJS.
* Support Standard Web Components.

<hr />

## Version 2.6

Version under development:

* Development: **Starting in July 2020**
* Estimated release date: **July 2021**
* Documentation: to be released [camptocamp.github.io/c2cgeoportal/master](https://camptocamp.github.io/c2cgeoportal/master/)

### Functionalities

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

* Release date: **23<sup>th</sup> April 2020**
* EOS: **October 2021**
* Documentation: [camptocamp.github.io/c2cgeoportal/2.5](https://camptocamp.github.io/c2cgeoportal/2.5/)

### Functionalities

1. Improve WMS browser (search, server list)
2. Map slider (swipe between maps)
3. Improve redlining, be able to define length, size
4. Close legend automatically when layer is deactivated
5. Display snappable layers and enable activation/deactivation
6. Intranet user panel
7. Show and validate mandatory fields in editing form
8. Timeslider improvements (dynamic map rendering)
9. Be able to define min and max scale for WMTS
10. Let filters active even if panel is closed
11. Query using a polygon
12. Global loading & counter message
13. Long name cut off in display window
14. Story maps
15. KML styling (import & export)
16. Be able to use desktop on a tablet
17. Geolocation on desktop interface
18. WMS GetFeatureInfo on non WFS servers
19. Security - No cached credentials
20. Security - Configurable account lockout
21. Security - Secure password storage
22. Security - Session timeouts
23. Architecture - Docker only

<hr />

## Version 2.4 (LTR)

* Release date: **7<sup>th</sup> July 2019**
* EOS: **July 2022**
* Documentation: [camptocamp.github.io/c2cgeoportal/2.4](https://camptocamp.github.io/c2cgeoportal/2.4/)

### Functionalities

1. IFRAME integration
2. Editing - Column order
3. Editing - Read only attributes
4. Editing - Link to external form
5. Drawing - Delete vertex menu
6. Drawing - Zoom on recenter
7. Read only drawing on mobile
8. Layer tree - Resize panel
9. Layer tree - Radio buttons
10. Query - Auto-link in results
11. Interface - App loading widget
12. Interface - mobile first level panel title
13. A0 printing

<hr />

## Version 2.3

* Release date: **23<sup>th</sup> Mai 2018**
* Documentation: [camptocamp.github.io/c2cgeoportal/2.3](https://camptocamp.github.io/c2cgeoportal/2.3/)

### Functionalities

1. WMS / KML browser integration + permalink
2. Map rotation
3. Moving Window & query result / resizing
4. Administration interface
5. Result window optimization
6. Layertree flush / no flush in mobile version
7. Opacity for layers in mobile version

<hr />

## Version 2.2

* Release date: **22 January 2018**
* Documentation: [camptocamp.github.io/c2cgeoportal/2.2](https://camptocamp.github.io/c2cgeoportal/2.2/)

### Functionalities

1. Query builder and filters
2. WFS query: take time into account
3. Not found text in fulltextsearch
4. Street View integration
5. Clear all button in layertree
6. User defined scales for printing
7. Android web browser compatibility
8. Predefined transparency for WMS / WMTS
