'use strict';

var setups = $('.setup');

/**
 * Add click handlers to each of the setups
 */
 function registerClickHandler() {
   setups.on('click', function() {
     return $(this).next().show()
 })
 };


// Register handlers for permanent elements on the page.
$(document).ready(registerClickHandler);
