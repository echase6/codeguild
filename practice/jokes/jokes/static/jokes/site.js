'use strict';

var setups = $('.setup');

/**
 * Add click handlers to each of the setups
 */
 var click_handler = setups.on('click', function() {
   return $(this).next().show()
 });

setups.append(click_handler)
