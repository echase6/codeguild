'use strict';


var setups = $('.setup');

/**
 * Add click handlers to each of the setups
 */
var punchShow = _.map(setups, function(setup_tag) {
  var click_handler = $(setup_tag).on('click', function() {
    return $(this).next().show()
  });
})

setups.append(punchShow)
