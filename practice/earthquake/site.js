'use strict';

var MS_IN_WK = 1000 * 60 * 60 * 24 * 7;
var DOT_SCALE = 50000;  /// Good number is 50000
var DOT_COLOR = '200, 128, 128';  ///'R, G, B'

/**
 * Makes Atom linter happier about the ol functions.
 */
if (!window.ol) {
  var ol;
}

/**
 * Function to load the earthquake data.  Uses a Promise.
 * @return {[json]} The data in JSON format
 */
function getEarthquakeJSON() {
  var url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: url,
  }));
}


/**
 * Create an OpenLayers map and return its identifier.
 */
function createMap() {
  var mapBackground = new ol.layer.Tile({
    source: new ol.source.OSM()
  });
  var map = new ol.Map({
    layers: [mapBackground],
    target: 'map',
    controls: ol.control.defaults({
      attributionOptions: {
        collapsible: false
      }
    }),
    view: new ol.View({
      center: [0, 0],
      zoom: 2
    })
  });
  $('#map').data('map', map);
  return map;
}

/**
 * Create an empty source to add the earthquate icons to.
 * @param  {ol.Map}      The Map element that will hold the source.
 * @return {ol.Source}   The source that will hold the icons.
 */
function createSource(map) {
  var vectorSource = new ol.source.Vector();
  var earthquakeLayer = new ol.layer.Vector({source: vectorSource});
  map.addLayer(earthquakeLayer);
  return vectorSource;
}

/**
 * Function to parse the JSON file and gather location, mag, and time/Date
 *   Filters out data with null values.
 * @param  {[JSON]}   The data from the earthquake reporting service
 * @return {[array]}  Array of arrays: [long, lat, mag, UTC]
 */
function scrapeEarthquakeData(json) {
  var data = _.map(json.features, function(feature) {
    return [feature.geometry.coordinates[0],
            feature.geometry.coordinates[1],
            feature.properties.mag,
            feature.properties.time
          ];
  });
  data = _.filter(data, function(feature) {
    return _.every(feature, function(item) {return item !== null;});
  });
  return data;
}

/**
 * Create an indiviual filled circle
 *    Radius is a function of the earthquake magnitude, larger = bigger.
 *    Opacity is a function of the age; new = more opaque.
 * @param  {array} data    Array holding [lon, lat, mag, time]
 * @return {ol.Feature}    The circle feature to be added to the collection.
 */
function createDot(feature) {
  var nowTime = Date.now();
  var circle = new ol.geom.Circle(
                ol.proj.fromLonLat([feature.geometry.coordinates[0],
                                    feature.geometry.coordinates[1]]),
                DOT_SCALE * feature.properties.mag,
                'XY'
              );
  var circleFeature = new ol.Feature(circle);
  var utcTime = feature.properties.time;
  var opacity = 1.0 - (nowTime - utcTime) / MS_IN_WK;  /// newer = opaquer
  var colorString = 'rgba(' + DOT_COLOR + ',' + opacity + ' )';
  circleFeature.setStyle(new ol.style.Style({
    fill: new ol.style.Fill({color: colorString})
  }));
  return circleFeature;
}

/**
 * Function to create a collection of Icons.
 * @param {[array]}         Array of arrays:  [long, lat, mag, UTC]]
 * @return {ol.Collection}  The collection element to be added to the source.
 */
function addIcons(data) {
  var iconCollection = new ol.Collection();
  _.forEach(data.features, function(item) {
    var circleFeature = createDot(item);
    iconCollection.push(circleFeature);
  });
  return iconCollection;
}

/**
 * Display the earthquakes on the map by its features.
 *   Clear it first in case this is called as an update.
 * @param  {[ol.Source]}  The vector source element
 * @param  {[array]}      Array of arrays [long, lat, mag, UTC]
 */
function displayEarthquakes(source, data) {
  var iconCollection = addIcons(data);
  source.clear();
  source.addFeatures(iconCollection.getArray());
}

/**
 * Overall function that gathers data and displays earthquake icons.
 *   Asychronously displays the earthquake icons using Promse - then.
 * @param  {[ol.source]} source element for icons.
 */
function runDisplayEarthquakes(source) {
  getEarthquakeJSON().
    then(function(earthquakeJSON) {
      // var earthquakeData = scrapeEarthquakeData(earthquakeJSON);
      displayEarthquakes(source, earthquakeJSON);
    }
  );
}

/**
 * The call-back function that updates the already existing map.
*/
function updateMap() {
  var map = $('#map').data('map');
  var source = map.getLayers().getArray()[1].getSource();
  runDisplayEarthquakes(source);
}

/**
 * Handlers for zoom-in/zoom-out buttons and 5-minute icon updates.
 * @param  {[ol.Map} map [map element]
 */
function registerMapEventHandlers(map) {
  document.getElementById('zoom-out').onclick = function() {
    var view = map.getView();
    var zoom = view.getZoom();
    view.setZoom(zoom - 1);
  };

  document.getElementById('zoom-in').onclick = function() {
    var view = map.getView();
    var zoom = view.getZoom();
    view.setZoom(zoom + 1);
  };
  var FIVE_MIN_IN_MS = 5 * 60 * 1000;
  var intervalID = window.setInterval(updateMap, FIVE_MIN_IN_MS);
}

/**
 * Overall main function that inits the map, registers buttons, displays icons.
 */
function runInitPage() {
  var map = createMap();
  var source = createSource(map);
  registerMapEventHandlers(map);
  runDisplayEarthquakes(source);
}


$(document).ready(runInitPage);
