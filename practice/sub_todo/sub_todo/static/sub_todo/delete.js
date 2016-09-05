'use strict';

$('.deleteTarget').on('click', function(event) {
  event.preventDefault()
  var target = event.currentTarget;
  runDelete(target).
  then(function() {
    window.location.reload()
  })
})
function runDelete(target) {
  return Promise.resolve($.ajax({
    url: $(target).attr('href'),
    method: 'DELETE',
  }));
}
