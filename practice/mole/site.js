'use strict';

var score = 0;

function createDivGrid() {
  var container = $('div');
  for (var i = 0; i < 5; i += 1) {
    container.append('<div class=row id=row' + i + '></div>');
    for (var j = 0; j < 4; j += 1) {
      var rowContainer = $('#row' + i);
      rowContainer.append('<div id=' + i + j + '></div>');
      var itemContainer = $('#' + i + j);
      itemContainer.append('<input type="image" src="./media/hole.jpg">');
    }
  }
}

function checkAllFilled() {
  var inputIds = $('input');
  return _.every(_.map(inputIds, function(e) {return $(e).attr('src') === './media/mole.jpg';}));
}

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}


function setRandomMole() {
  var i = getRandomInt(5);
  var j = getRandomInt(4);
  var itemContainer = $('#' + i + j + ' > input');
  while (itemContainer.attr('src') === './media/mole.jpg' & !checkAllFilled()) {
    var i = getRandomInt(5);
    var j = getRandomInt(4);
    var itemContainer = $('#' + i + j + ' > input');
  }
  itemContainer.attr('src', './media/mole.jpg');
  var moleAudioTag = new Audio('./media/mole.mp3');
  moleAudioTag.volume = 0.5;
  moleAudioTag.play();
}

function updateScore() {
}


function myCallback() {
  var that = this;
  if (checkAllFilled()) {
    clearInterval(that);
  } else {
    setRandomMole();
  }
}


function speedUp(intervalID) {
  // var moleIntervalMs = 1000;
  var that = this;
  if (checkAllFilled()) {
    clearInterval(that);
  } else {
    clearInterval(intervalID)
    // intervalID = window.setInterval(myCallback, 1000);
    // interval = interval;
  }
}

function registerEventHandlers() {
  // var intervalID = window.setInterval(myCallback, 1000);
  createDivGrid();
  var bgAudioTag = new Audio('./media/background.mp3');
  bgAudioTag.loop = true;
  bgAudioTag.volume = .15;
  bgAudioTag.play();
  var moleIntervalMs = 1000;
  var speedUpIntervalMs = 2000;
  var intervalID = window.setInterval(myCallback, 1000);
  // var speedUpIntervalID = window.setInterval(speedUp(intervalID), speedUpIntervalMs);
  $('input').click(function() {
    if ($(this).attr('src') === './media/mole.jpg') {
      $(this).attr('src', './media/hole.jpg');
      var hitAudioTag = new Audio('./media/hit.mp3');
      hitAudioTag.volume = 1.0;
      hitAudioTag.play();
      score += 100;
      $('h2').text('Score: ' + score)
    } else {
      var missAudioTag = new Audio('./media/miss.mp3');
      missAudioTag.volume = 1.0;
      missAudioTag.play();
      score -= 50;
      $('h2').text('Score: ' + score)
    }
  });
  // var gameOver = checkAllFilled();
  // while (!checkAllFilled()) {
  //   updateScore();
  // }
  // clearInterval(speedUpIntervalID);
  // clearInterval(moleIntervalID);
}

function speedUp(intId, intMs) {
  clearInterval(intId);
  intMs = intMs * 0.9;
  intId = window.setInterval(setRandomMole(), intMs);
}

//
// var intervalID = window.setInterval(myCallback, 1000);
// createDivGrid();
// var bgAudioTag = new Audio('./background.mp3');
// bgAudioTag.loop = true;
// bgAudioTag.volume = .15;
// bgAudioTag.play();


// $('input').click(function() {
//   $(this).attr('src', './hole.jpg')
// })

$(document).ready(registerEventHandlers);
