'use strict';

$('form').on('submit', function(event) {
  event.preventDefault()
  var flutt_text = $('textfield').text;
  runSubmit(flutt_text)
  })
})
function runSubmit(flutt_text) {
  $.ajax({
    url: $(target).attr('href'),
    method: 'POST',
  });
}
