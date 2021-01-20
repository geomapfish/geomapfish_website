Title: Fonctionnalités
Date: 2016-10-14
Modified: 2020-03-19
Authors: Michael Kalbermatten, Rémi Bovard
URL: functionalities
Save_as: functionalities.html
Slug: 1_functionalities
Lang: fr
<br />
GeoMapFish est composé d'une interface desktop, d'administration, d'une API pour une intégration
dans des sites connexes et d'une version mobile.

En plus des webservices aux standards OGC, un protocole MapFish est disponible. Ce dernier
est adapté pour une communication efficiente entre client et serveur. Sur cette base, des applications
complexes et performantes peuvent être mises en place.

GeoMapFish combine quelques-uns des meilleurs outils OpenSource en une seule application:

* [OpenLayers](https://openlayers.org/), [AngularJS](https://angularjs.org/) et [ngeo](https://camptocamp.github.io/ngeo/master/apidoc/) pour la partie cliente
* Modules Python (spécialement ceux liés à [Pyramid](https://trypyramid.com/)) pour la partie serveur
* [MapFish Print](https://mapfish.github.io/mapfish-print-doc/), un servlet Java dédié à l'impression de documents contenant de la cartographie.

## Documentation et support

Les différents composants de GeoMapFish sont:

* La dernière version de la documentation se trouve [ici](https://camptocamp.github.io/c2cgeoportal/master/)
* La partie serveur de GeoMapFish est [c2cgeoportal](https://github.com/camptocamp/c2cgeoportal/) 
* La partie cliente de GeoMapFish est une librairie AngularJS appelée [ngeo](https://github.com/camptocamp/ngeo/)

## GeoMapFish Viewer

### ![Functionalities description]({filename}/images/1_1_responsive.png) Interface utilisateur

* Interface "responsive" en version desktop & mobile

### ![Functionalities description]({filename}/images/1_2_search.png) Recherche Full text

* Données
* Couches
* Thème

### ![Functionalities description]({filename}/images/1_3_navigation.png) Navigation

* Zoom & pan
* Barre de navigation
* Geolocalisation

### ![Functionalities description]({filename}/images/1_4_query.png) Requête

* Interrogation ponctuelle & rectangulaire
* Résultat sous forme de table et/ou de fenêtre
* Interrogation de coordonnées et de données raster en temps réel

### ![Functionalities description]({filename}/images/1_5_data.png) Données

* WMS & WMTS internes
* WMS-T
* Données externes (WMS, KML)
* Organisation en thèmes
* Ajout de couches dans les thèmes
* Transparency & metadata
* Légende dynamique

### ![Functionalities description]({filename}/images/1_6_print.png) Impression

* Impression en PDF & PNG

### ![Functionalities description]({filename}/images/1_7_drawing.png) Dessin & mesure

* Points
* Lignes
* Surfaces
* Rectangles
* Cercles (azimut)
* Etiquettes

### ![Functionalities description]({filename}/images/1_8_layer_editing.png) Edition de couches

* Edition simple dans la BD
* Configuration simple
* Edition complexe (accroché, copié, coupé, extraction de donut)

### ![Functionalities description]({filename}/images/1_9_gis.png) Fonctionnalités SIG

* Requêtes SQL & filtres
* Curseurs temporels

### ![Functionalities description]({filename}/images/1_10_misc.png) Autre

* Profil
* Intégration de Google StreetView
* Permalien
* URL courte de type permalien

---

## Administration GeoMapFish

### ![Functionalities description]({filename}/images/2_1_configuration.png) Administration des données

* Configuration de couches
* Configuration de groupes de couches
* Configuration de thèmes
* Configuration des sources de données

### ![Functionalities description]({filename}/images/2_2_authentication.png) Authentification

* LDAP, NTLM et autres systèmes possibles

### ![Functionalities description]({filename}/images/2_3_roles.png) Rôles

* Configuration de rôles
* Configuration des utilisateurs
* Configuration d'aires de restriction
* Configuration de fonctionnalités liées à l'utilisateur

---

## Partie serveur de GeoMapFish

### ![Functionalities description]({filename}/images/3_1_pdf.png) Création de rapport PDF

### ![Functionalities description]({filename}/images/3_2_webmapping.png) Backends de cartographie web

* MapServer
* QGIS Server
* ArcGIS for Server

### ![Functionalities description]({filename}/images/3_3_docker.png) Déploiement Docker

<br /><br />
Une meilleure vue d'ensemble des fonctionnalités et versions est donnéee sur la [page des features](https://github.com/camptocamp/ngeo/blob/master/docs/features.md).
