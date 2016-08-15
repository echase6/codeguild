'use strict';

/**
 * [getBusRoutes description]
 * @param  {[type]} location [description]
 * @return {[type]}          [description]
 */
function getBusRoutes(location) {
  var PARAMS = {
    appID: '901D615BDE940B4551D82DB15',
    ll: location,
    meters: 2000,
    showRoutes: true,
    json: true
  };
  var url = 'https://developer.trimet.org/ws/V1/stops';
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: url,
    data: PARAMS
  }));
}

/**
 * [formatBusRoutes description]
 * @param  {[type]} atLocationObject [description]
 * @return {[type]}                  [description] */
function scrapeBusRoutes(atLocationObject) {
  var stopsList = atLocationObject.resultSet.location;
  console.dir(stopsList);
  var filteredStops = _.filter(stopsList,
    function(object) {return _.has(object, 'route');});
  var routesByStops = _.map(filteredStops, function(object) {
    return object.route;
  });
  console.dir(routesByStops);
  var flatRoutesByStops = _.flatten(routesByStops);
  var busRoutesByStops = _.filter(flatRoutesByStops, function(object) {
    return object.desc.match(/^\d/);
  });
  console.dir(busRoutesByStops);
  // var routesList = _.map(busRoutesByStops, function(obj) {
  //   return [obj.route, ;
  // });
  var uniqueRoutes = _.uniqBy(busRoutesByStops, function(object) {
    return object.route;
  });
  console.dir(uniqueRoutes);
  return uniqueRoutes;
}

function insertRoutes(routes) {
  var ul = $('ul');
  ul.children().remove();
  _.each(routes, function(line) {
    var li = $('<li></li>');
    var a = $('<a></a>');
    var paddedRouteNumber = ('000' + line.route).substr(-3);
    a.attr('href', 'http://trimet.org/schedules/r' + paddedRouteNumber);
    a.text(line.desc);
    li.append(a);
    ul.append(li);
  });

}

/**
 * [getLocation description]
 * @return {[type]} [description]
 */
function main() {
  navigator.geolocation.getCurrentPosition(function(position) {
    getBusRoutes([position.coords.latitude, position.coords.longitude].
      join(',')).
    then(function(object) {
      var uniqueRoutes = scrapeBusRoutes(object);
      insertRoutes(uniqueRoutes);
    });
    var li = $('<li>Loading...</li>');
    $('ul').append(li);
  });
}

/**
 *
 */

$(document).ready(main);
