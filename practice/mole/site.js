'use strict';

function createDivGrid() {
  var container = $('div');
  for (var i = 0; i < 5; i += 1) {
    container.append('<div class=row id=row' + i + '></div>');
    for (var j = 0; j < 4; j += 1) {
      var rowContainer = $('#row' + i);
      rowContainer.append('<div id=' + i + j + '></div>');
      var itemContainer = $('#' + i + j);
      itemContainer.append('<input type="image" src="./hole.jpg">');
    }
  }
}


function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}


function setRandomMole() {
  var i = getRandomInt(0, 5);
  var j = getRandomInt(0, 4);
  var itemContainer = $('#' + i + j + ' > input');
  itemContainer.attr('src', './mole.jpg');
}

function registerEventHandlers() {
  $('#form-submit').on('submit', function(event) {
    event.preventDefault();
    createDivGrid();
  });
}

function myCallback() {
  setRandomMole();
}

var intervalID = window.setInterval(myCallback, 1000);

createDivGrid();

$(document).ready(registerEventHandlers);
