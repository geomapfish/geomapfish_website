Title: GeoMapFish
Date: 2016-10-14
Modified: 2017-08-21
Authors: Michael Kalbermatten, Rémi Bovard
URL: index.html
Save_as: index.html
Slug: 0_index
Lang: fr
Menulabel: Accueil
<br>
Bienvenue sur le site web de la communauté GeoMapFish (GMF), merci de votre visite !

Le framework GMF permet de construire des applications WebSIG de manière aisée et flexible.
Il est composé d'une interface desktop, d'administration, d'une API pour une intégration
dans des sites connexes et d'une version mobile.

En plus des webservices aux standards OGC, un protocole MapFish est disponible. Ce dernier
est adapté pour une communication efficiente entre client et serveur. Sur cette base, des applications
complexes et performantes peuvent être mises en place.

GeoMapFish combine quelques-uns des meilleurs outils OpenSource en une seule application:

* Version 1: [OpenLayers 2](https://openlayers.org/two/), [ExtJS](https://docs.sencha.com/extjs/3.4.0/) et [GeoExt](http://geoext.org/v1/) pour la partie cliente
* Version 2: [OpenLayers](https://openlayers.org/), [AngularJS](https://angularjs.org/) et [ngeo](https://camptocamp.github.io/ngeo/master/apidoc/) pour la partie cliente
* Modules Python (spécialement ceux liés à [Pyramid](https://trypyramid.com/)) pour la partie serveur
* [MapFish Print](https://mapfish.github.io/mapfish-print-doc/), un servlet Java dédié à l'impression de documents contenant de la cartographie.

## Documentation et support

Les différents composants de GeoMapFish sont:

* La partie serveur de GeoMapFish est [c2cgeoportal](https://github.com/camptocamp/c2cgeoportal/) 
* La partie cliente de GeoMapFish 2.x est une librairie AngularJS appelée [ngeo](https://github.com/camptocamp/ngeo/)
* La partie cliente de GeoMapFish 1.x est une librairie ExtJS appelée [CGXP](https://github.com/camptocamp/cgxp/)

<br><br>
![Example screenshot]({filename}/images/examples/demo22.png)
