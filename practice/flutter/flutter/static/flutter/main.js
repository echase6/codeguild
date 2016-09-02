'use strict';

var sourceForm = $('#flutter-form');

sourceForm.on('submit', function(event) {
  event.preventDefault();
  runSubmitAndUpdate();
  window.location.href = sourceForm.attr('nextaction');
  })


function runSubmitAndUpdate() {
  var actionURL = sourceForm.attr('action');
  var submitMethod = sourceForm.attr('method');
  var formData = sourceForm.serialize();
  console.dir(formData);
  // return Promise.resolve($.ajax({
  $.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  })
// );
}
