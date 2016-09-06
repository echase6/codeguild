'use strict';

function initMap() {
    var ll = new google.maps.LatLng(LAT, LNG);
    var options = { zoom: 8, center: ll, mapTypeId: 'satellite' };
    var map = new google.maps.Map(document.getElementById('map'), options);
    var marker = new google.maps.Marker({
    position: ll,
    map: map,
    title: 'Here they are!'
    });
    marker.setMap(map);
   }