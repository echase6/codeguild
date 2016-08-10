'use strict';

/**
 * [getURL description]
 * @return {[type]} [description]
 */
function getURL() {
  return $('#URL-getter').val();
}


function countImages() {
  var itemCount = $('div > div').length;
  $('h2').text('Number of images: ' + itemCount);
}


function createThumbNail(URL) {
  var thumbImage = $('<img>');
  thumbImage.attr('src', URL);
  return thumbImage;
}

function createUrlTag(URL) {
  var UrlTag = $('<a href="' + URL + '">Expand</a>');
  return UrlTag;
}

function createRemoveBox(tileItem) {
  var killLink = $('<button type="button">X</button>');
  killLink.on('click', function(event) {
    event.preventDefault();
    runRemoveTile(tileItem);
  });
  return killLink;
}

function addTile(tileItem) {
  $('section > div').append(tileItem);
  countImages();
}


/**
 * [createTile description]
 * @return {[type]} [description]
 */
function createTile(URL) {
  var thumbNail = createThumbNail(URL);
  var UrlTag = createUrlTag(URL);
  var tile = $('<div></div>');
  tile.append(thumbNail);
  tile.append(UrlTag);
  var removeBox = createRemoveBox(tile);
  tile.append(removeBox);
  return tile;
}


function inputTile() {
  var userURL = getURL();
  var tileItem = createTile(userURL);
  addTile(tileItem);
}

function runRemoveTile(tile) {
  tile.remove();
  countImages();
}


function registerEventHandlers() {
  $('#form-submit').on('submit', function(event) {
    event.preventDefault();
    inputTile();
  });
}

$(document).ready(registerEventHandlers);
