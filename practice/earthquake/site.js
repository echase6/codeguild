'use strict';

var MS_IN_WK = 1000 * 60 * 60 * 24 * 7;

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
  return map;
}

/**
 * Creates the Icon Layer, from the collection of icons.
 * @param  {[o.Collection]} iconCollection [the collection of icons]
 * @return {[ol.layer]}     the layer to be added to the map.
 */
function createIconLayer(iconCollection) {
  var vectorSource = new ol.source.Vector({
    features: iconCollection
  });
  var earthquakeLayer = new ol.layer.Vector({
    source: vectorSource
  });
  return vectorSource, earthquakeLayer;
}

/**
 * Function to parse the JSON file and gather location, mag, and time/date
 * @param  {[JSON]} json [the data from the earthquake reporting service]
 * @return {[array]}      [array of arrays: [long, lat, mag, date]]
 */
function getEarthquakeData(json) {
  var data = _.map(json.features, function(feature) {
    return [feature.geometry.coordinates[0],
            feature.geometry.coordinates[1],
            feature.properties.mag,
            feature.properties.time
          ];
  });
  // console.log(data);
  return data;
}

/**
 * Function to create a collection of Icons.
 * @param {[array]} data [array of arrays:  [long, lat, mag, date]]
 */
function addIcons(data) {
  var nowTime = Date.now();
  var iconCollection = new ol.Collection();
  _.forEach(data, function(item) {
    var circle = new ol.geom.Circle(
                  ol.proj.fromLonLat([item[0], item[1]]),
                  50000 * item[2],
                  'XY'
                );
    var circleFeature = new ol.Feature(circle);
    var opacity = 1.0 - (nowTime - item[3]) / MS_IN_WK;
    var colorString = 'rgba(128, 128, 128, ' + opacity + ' )';
    circleFeature.setStyle(new ol.style.Style({
      fill: new ol.style.Fill({color: colorString})
    }));
    iconCollection.push(circleFeature);
  });
  return iconCollection;
}

/**
 * Display the earthquakes on the map by adding the Icon layer to it.
 * @param  {[ol.Map]} map  [The displayed map element; edits in-place]
 * @param  {[array]} data [array of arrays [long, lat, mag, date]]
 */
function displayEarthquakes(map, data) {
  var iconCollection = addIcons(data);
  var iconLayer = createIconLayer(iconCollection);
  map.addLayer(iconLayer);
}

/**
 * Overall function that gathers data and displays earthquake icons.
 * @param  {[ol.Map]} map [Displayed map element]
 */
function runDisplayEarthquakes(map) {
  getEarthquakeJSON().
    then(function(earthquakeJSON) {
      var earthquakeData = getEarthquakeData(earthquakeJSON);
      displayEarthquakes(map, earthquakeData);
    }
  );
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
}

/**
 * Overall main function that inits the map, registers buttons, displays icons.
 */
function runInitPage() {
  var map = createMap();
  registerMapEventHandlers(map);
  runDisplayEarthquakes(map);
}


$(document).ready(runInitPage);
