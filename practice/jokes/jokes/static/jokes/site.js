'use strict';


var setups = $('.setup');

/**
 * Show the punchline.
 */
function showPunchline() {
    $(this).next().show();
}


function registerEventHandlers() {
  setups.on('click', showPunchline);
}


$(document).ready(function() {
  registerEventHandlers();
  setups.next().hide();
});
