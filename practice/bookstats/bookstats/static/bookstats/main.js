'use strict';

var sourceForm = $('form');


function runQuery(event) {
  console.log('running query');
  event.preventDefault();
  var actionURL = sourceForm.attr('action');
  var submitMethod = sourceForm.attr('method');
  // This takes the data from the form and packages it up for sending.
  var formData = sourceForm.serialize();
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  })).then(function (json) {
    display_results(json);
  });
}

function display_results(json) {
    var search_text = [
      'Search: ',
      json.word,
      ', count: ',
      json.word_count,
      ', freq: ',
      json.word_freq * 100,
      '%'
  ].join('')

  var item = $('<li>').text(search_text).on(
    'click',
    function(event) {
      $(event.currentTarget).remove();
    }
  );
  $('ul').append(item);
}


function registerEventHandlers() {
  console.log('hi');
  sourceForm.on('submit', runQuery);
}

$(document).ready(registerEventHandlers);
