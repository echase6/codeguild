'use strict';

/**
 * Completer object contains completions.
 *
 * completions will have keys as the completion and values as weights.
 */
function Completer() {
  this.completions = {};
}

var modifyCompleter = {
  addCompletion: function(str) {
    this.completions[str] = 1;
  },
  removeCompletion: function(str) {
    delete this.completions[str];
  },
  complete: function(prefix) {
    var re = RegExp('^' + prefix);
    var matches = _.pickBy(this.completions,
      function(v, k) {return re.test(k);});
    return _.keys(matches);
  }
};

Completer.prototype = modifyCompleter;

var textCompleter = new Completer();

textCompleter.addCompletion('eric');
textCompleter.addCompletion('google');
textCompleter.addCompletion('dolly');
textCompleter.removeCompletion('eric');
textCompleter.addCompletion('dollar');


var matches = textCompleter.complete('dol');

console.dir(matches);
