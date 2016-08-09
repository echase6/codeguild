'use strict';

/**
 * Completer object contains completions.
 *
 * completions will have keys as the completion and values as weights.
 */
function Completer() {
  this.completions = {};
}

/**
 * modifyCompleter has these methods:
 *
 * addCompletion() adds a completion to the completions container (in-place)
 * removeCompletion() removes a completion from the container (in-place)
 * complete() returns an array of completions, highest weighted first
 * selectCompletion() increases the weight of a given completion (in-place)
 *
 */
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
    var sortedMatches = _.map(_.orderBy(_.toPairs(matches),
                                        function(o) {return o[1];}, 'desc'),
                              function(o) {return o[0];});
    return sortedMatches;
  },
  selectCompletion: function(str) {
    this.completions[str] += 1;
  }
};

Completer.prototype = modifyCompleter;

var textCompleter = new Completer();

textCompleter.addCompletion('eric');
textCompleter.addCompletion('google');
textCompleter.addCompletion('dolly');
textCompleter.removeCompletion('eric');
textCompleter.addCompletion('dollar');
textCompleter.selectCompletion('dolly');
textCompleter.selectCompletion('dolly');


var matches = textCompleter.complete('dol');
console.dir(matches);
