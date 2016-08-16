'use strict';

var MS_IN_WK = 1000 * 60 * 60 * 24 * 7;
var DOT_SCALE = 50000;  /// Good number is 50000
var DOT_COLOR = '200, 128, 128';  ///'R, G, B'

if (!window.ol) {
  var ol;
}

/**
 * Function to load the earthquake data.  Uses a Promise.
 * @return {[json]} [the data in JSON format]
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
 * [createSource description]
 * @param  {[type]} map [description]
 * @return {[type]}     [description]
 */
function createSource(map) {
  var vectorSource = new ol.source.Vector();
  var earthquakeLayer = new ol.layer.Vector({source: vectorSource});
  map.addLayer(earthquakeLayer);
  return vectorSource;
}

/**
 * Function to parse the JSON file and gather location, mag, and time/date
 * @param  {[JSON]} json [the data from the earthquake reporting service]
 * @return {[array]}      [array of arrays: [long, lat, mag, UTC]]
 */
function scrapeEarthquakeData(json) {
  var data = _.map(json.features, function(feature) {
    return [feature.geometry.coordinates[0],
            feature.geometry.coordinates[1],
            feature.properties.mag,
            feature.properties.time
          ];
  });
  return data;
}

/**
 * Function to create a collection of Icons.
 * @param {[array]} data [array of arrays:  [long, lat, mag, UTC]]
 */
function addIcons(data) {
  var nowTime = Date.now();
  var iconCollection = new ol.Collection();
  _.forEach(data, function(item) {
    var circle = new ol.geom.Circle(
                  ol.proj.fromLonLat([item[0], item[1]]),
                  DOT_SCALE * item[2],
                  'XY'
                );
    var circleFeature = new ol.Feature(circle);
    var opacity = 1.0 - (nowTime - item[3]) / MS_IN_WK;  /// newer = opaquer
    var colorString = 'rgba(' + DOT_COLOR + ',' + opacity + ' )';
    circleFeature.setStyle(new ol.style.Style({
      fill: new ol.style.Fill({color: colorString})
    }));
    iconCollection.push(circleFeature);
  });
  return iconCollection;
}

/**
 * Display the earthquakes on the map by its features.
 * @param  {[ol.Source]}   [The vector source element]
 * @param  {[array]} data [array of arrays [long, lat, mag, UTC]]
 */
function displayEarthquakes(source, data) {
  var iconCollection = addIcons(data);
  source.clear();
  source.addFeatures(iconCollection.getArray());
}

/**
 * Overall function that gathers data and displays earthquake icons.
 * @param  {[ol.Map]} map [Displayed map element]
 */
function runDisplayEarthquakes(source) {
  getEarthquakeJSON().
    then(function(earthquakeJSON) {
      var earthquakeData = scrapeEarthquakeData(earthquakeJSON);
      displayEarthquakes(source, earthquakeData);
    }
  );
}

/**
 * [The call-back function that updates the already existing map.]
*/
function updateMap() {
  var map = $('#map').data('map');
  var source = map.getLayers().getArray()[1].getSource();
  runDisplayEarthquakes(source);
}

/**
 * Handlers for zoom-in/zoom-out buttons
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
  var intervalID = window.setInterval(updateMap, 10000);
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
