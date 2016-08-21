'use strict';

var score = 0;
/**
 * Creates a grid of holes, along with class tags.
 */
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

/**
 * Checks is all locations are filled with moles.
 * @return {boolean} True if all filled.
 */
function checkAllFilled() {
  var inputIds = $('input');
  return _.every(_.map(inputIds, function(e) {
    return $(e).attr('src') === './media/mole.jpg';
  }));
}

/**
 * Get and return a random integer.
 */
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

/**
 * Put a mole in a random location.
 *   It seeks empty locations.  If all are filled, it silently ends.
 */
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

/**
 * Callback routine for adding a mole.  If all are filled, it clears
 *   the timing interval, although this is not permanent.
 */
function myCallback() {
  var that = this;
  if (checkAllFilled()) {
    clearInterval(that);
  } else {
    setRandomMole();
  }
}

/**
 * Master interval, for decreasing the mole-placement interval.
 *   Currently not working so it is not being called.
 * @param  {integer} intervalID The interval to decrease the interval.
 */
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

/**
 * Do this if mole is hit:
 *   change image to hole
 *   play a successful hit .mp3
 *   increase the score
 * @param  {holeTag} The tag of the sucessful hit.
 */
function toDoIfHit(holeTag) {
  $(holeTag).attr('src', './media/hole.jpg');
  var hitAudioTag = new Audio('./media/hit.mp3');
  hitAudioTag.volume = 1.0;
  hitAudioTag.play();
  score += 100;
  $('h2').text('Score: ' + score);
}

/**
 * Set up the game grid and start the background music.
 */
function setUpGame() {
  createDivGrid();
  var bgAudioTag = new Audio('./media/background.mp3');
  bgAudioTag.loop = true;
  bgAudioTag.volume = .15;
  bgAudioTag.play();
}

/** Do this if user hit a hole, not a mole:
 *    play a miss .mp3
 *    decrease the score
 *
 */
function toDoIfMiss() {
  var missAudioTag = new Audio('./media/miss.mp3');
  missAudioTag.volume = 1.0;
  missAudioTag.play();
  score -= 50;
  $('h2').text('Score: ' + score);
}

function registerEventHandlers() {
  // var intervalID = window.setInterval(myCallback, 1000);
  setUpGame();
  // var speedUpIntervalMs = 2000;
  var intervalID = window.setInterval(myCallback, 1000);
  // var speedUpIntervalID = window.setInterval(speedUp(intervalID), speedUpIntervalMs);
  $('input').click(function() {
    if ($(this).attr('src') === './media/mole.jpg') {
      toDoIfHit(this);
    } else {
      toDoIfMiss();
    }
  });
  // var gameOver = checkAllFilled();
  // while (!checkAllFilled()) {
  //   updateScore();
  // }
  // clearInterval(speedUpIntervalID);
  // clearInterval(moleIntervalID);
}

$(document).ready(registerEventHandlers);
